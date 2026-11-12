---
template: false
document_kind: "source-example"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
message_ids: ["auth.050.001.01"]
literal_namespace: "urn:iso:std:iso:20022:tech:xsd:auth.050.001.01"
source_locations: [{"source_id": "src-000320", "heading_path": ["Business Examples", "Reference Data", "auth.050.001.01"], "heading_paragraph": "P551", "xml_first_paragraph": "P555", "xml_last_paragraph": "P565", "rendered_file_pages": [50, 51]}]
issue_ids: []
limitations: ["Heading and literal namespace remain independent source claims. No example namespace, value or structure has been rewritten."]
---

# Source example — auth.050.001.01

[src-000320](../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md); heading P551; XML P555–P565; Word file pages 50–51.

**P552** Description

**P553** The following MessageInstance provides an example of the Reference Instrument Classification message that is distributed to Competent Authorities.

**P554** Message Instance

## Literal source XML

```xml
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="urn:iso:std:iso:20022:tech:xsd:auth.050.001.01">
	<FinInstrmRptgInstrmClssfctnRpt>
		<InstrmClssfctn>
			<Idr>ESVTOB</Idr>
			<VldtyPrd>
				<FrDt>2007-07-01</FrDt>
			</VldtyPrd>
			<LastUpdtd>2007-07-01</LastUpdtd>
		</InstrmClssfctn>
	</FinInstrmRptgInstrmClssfctnRpt>
</Document>
```

## Checks and limitations

| Check | Result |
| --- | --- |
| XML well-formedness | pass |
| Heading definition | auth.050.001.01 |
| Literal namespace | urn:iso:std:iso:20022:tech:xsd:auth.050.001.01 |
| Heading/namespace agreement | pass |
| Exact literal-namespace schema validation | pass |


[Canonical supplied definition named by heading](../../../../messages/auth.050.001.01/index.md) · [Detailed test evidence and errors](../../../../../../../tracking/reviews/fitrr-context-tables-examples.json)

The source example is preserved exactly. A valid XML document is not necessarily valid against the schema. A mismatched namespace is not silently updated to the heading version.
