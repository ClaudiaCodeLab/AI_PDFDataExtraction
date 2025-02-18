import os
import tempfile
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.document_loaders import PyPDFLoader
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser

st.set_page_config(
    page_title="Solicitud de Préstamo Bancario | Extracción de Datos por LLM"
)

st.header('Solicitud de Préstamo Bancario')

st.subheader('Extracción de Datos por LLM')

profile_file = st.file_uploader("Sube un archivo en PDF para extraer la información del cliente", type=["pdf"])

if profile_file is not None:

    with st.spinner('Procesando la solicitud...'):

        with tempfile.NamedTemporaryFile(delete=False) as temporary_file:
            temporary_file.write(profile_file.read())

        loader = PyPDFLoader(temporary_file.name)
        text_profile = loader.load()

        edad = ResponseSchema(name="edad", description="¿Cuál es la edad del solicitante? Responde null si no está claro.")
        estudios = ResponseSchema(name="estudios", description="¿Cuál es el nivel de estudios del solicitante? Responde null si no está claro.")
        antiguedad = ResponseSchema(name="antiguedad", description="¿Cuántos meses de antigüedad laboral tiene el solicitante? Responde null si no está claro.")
        ingresos = ResponseSchema(name="ingresos", description="¿Cuáles son los ingresos netos medios mensuales de los últimos 12 meses? Responde null si no está claro.")
        saldo = ResponseSchema(name="saldo", description="¿Cuál es el saldo total en efectivo entre todas las cuentas bancarias? Responde null si no está claro.")
        gastos = ResponseSchema(name="gastos", description="¿Cuáles son los gastos medios mensuales de los últimos 12 meses? Responde null si no está claro.")

        response_schemas = [edad, estudios, antiguedad, ingresos, saldo, gastos]

        output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
        format_instructions = output_parser.get_format_instructions()

        template = """
        Este documento es un perfil de usuario para una solicitud de préstamo bancario, extrae la siguiente información:
        edad, estudios, antiguedad, ingresos, saldo, gastos
        texto: {text}
        {format_instructions}
        """

        prompt_template = ChatPromptTemplate.from_template(template=template)
        
        format_template = prompt_template.format_messages(text=text_profile, format_instructions=format_instructions)
        chat = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), temperature=0)
        response = chat(format_template)
        json_profile = output_parser.parse(response.content)

        st.write('Aquí está la información extraída del cliente en formato JSON:')
        st.json(json_profile)

        os.remove(temporary_file.name)