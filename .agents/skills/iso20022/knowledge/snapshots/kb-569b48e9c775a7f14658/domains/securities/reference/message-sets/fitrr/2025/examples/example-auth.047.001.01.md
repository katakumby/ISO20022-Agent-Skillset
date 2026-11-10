---
template: false
document_kind: "source-example"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
message_ids: ["auth.047.001.01"]
literal_namespace: "urn:iso:std:iso:20022:tech:xsd:auth.047.001.01"
source_locations: [{"source_id": "src-000320", "heading_path": ["Business Examples", "Reference Data", "auth.047.001.01"], "heading_paragraph": "P479", "xml_first_paragraph": "P483", "xml_last_paragraph": "P498", "rendered_file_pages": [48, 49]}]
issue_ids: []
limitations: ["Heading and literal namespace remain independent source claims. No example namespace, value or structure has been rewritten."]
---

# Source example — auth.047.001.01

[src-000320](../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md); heading P479; XML P483–P498; Word file pages 48–49.

**P480** Description

**P481** The following MessageInstance provides an example of the Reference Country Code message that is distributed to Competent Authorities.

**P482** Message Instance

## Literal source XML

```xml
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="urn:iso:std:iso:20022:tech:xsd:auth.047.001.01">
	<FinInstrmRptgCtryCdRpt>
		<CtryData>
			<Ctry>
				<Cd>DE</Cd>
				<Nm>Germany</Nm>
			</Ctry>
			<EEACtry>true</EEACtry>
			<Mod>NOCH</Mod>
			<VldtyPrd>
				<FrDt>2013-01-17</FrDt>
			</VldtyPrd>
			<LastUpdtd>2013-01-17</LastUpdtd>
		</CtryData>
	</FinInstrmRptgCtryCdRpt>
</Document>
```

## Checks and limitations

| Check | Result |
| --- | --- |
| XML well-formedness | pass |
| Heading definition | auth.047.001.01 |
| Literal namespace | urn:iso:std:iso:20022:tech:xsd:auth.047.001.01 |
| Heading/namespace agreement | pass |
| Exact literal-namespace schema validation | pass |


[Canonical supplied definition named by heading](../../../../messages/auth.047.001.01/index.md) · [Detailed test evidence and errors](../../../../../../../tracking/reviews/fitrr-context-tables-examples.json)

The source example is preserved exactly. A valid XML document is not necessarily valid against the schema. A mismatched namespace is not silently updated to the heading version.
