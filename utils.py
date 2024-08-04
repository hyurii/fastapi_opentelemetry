from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource


def init_otel():
    COLLECTOR_ENDPOINT = "localhost"
    COLLECTOR_PORT = 4318

    resource = Resource(
        attributes={"service.name": "my-cool-microservice", "os-version": "1.0.2", "cluster": "A", "datacentre": "BNE"}
    )
    provider = TracerProvider(resource=resource)
    processor = BatchSpanProcessor(OTLPSpanExporter(endpoint=f"http://{COLLECTOR_ENDPOINT}:{COLLECTOR_PORT}/v1/traces"))
    provider.add_span_processor(processor)

    # Sets the global default tracer provider
    trace.set_tracer_provider(provider)
