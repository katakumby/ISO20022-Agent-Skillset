---
template: false
document_kind: "source-example"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
message_ids: ["auth.048.001.01"]
literal_namespace: "urn:iso:std:iso:20022:tech:xsd:auth.048.001.01"
source_locations: [{"source_id": "src-000320", "heading_path": ["Business Examples", "Reference Data", "auth.048.001.01"], "heading_paragraph": "P499", "xml_first_paragraph": "P503", "xml_last_paragraph": "P523", "rendered_file_pages": [49]}]
issue_ids: []
limitations: ["Heading and literal namespace remain independent source claims. No example namespace, value or structure has been rewritten."]
---

# Source example — auth.048.001.01

[src-000320](../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md); heading P499; XML P503–P523; Word file pages 49–49.

**P500** Description

**P501** The following MessageInstance provides an example of the Reference Currency Code message that is distributed to Competent Authorities.

**P502** Message Instance

## Literal source XML

```xml
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="urn:iso:std:iso:20022:tech:xsd:auth.048.001.01">
	<FinInstrmRptgCcyCdRpt>
		<CcyData>
			<Ccy>
				<Cd>IRL</Cd>
				<Nm>Ireland</Nm>
			</Ccy>
			<FrctnlDgt>2</FrctnlDgt>
			<CtryDtls>
				<Cd>IE</Cd>
				<Nm>Ireland</Nm>
			</CtryDtls>
			<PreEuro>true</PreEuro>
			<Mod>NOCH</Mod>
			<VldtyPrd>
				<ToDt>2003-01-01</ToDt>
			</VldtyPrd>
			<LastUpdtd>2003-01-01</LastUpdtd>
		</CcyData>
	</FinInstrmRptgCcyCdRpt>
</Document>
```

## Checks and limitations

| Check | Result |
| --- | --- |
| XML well-formedness | pass |
| Heading definition | auth.048.001.01 |
| Literal namespace | urn:iso:std:iso:20022:tech:xsd:auth.048.001.01 |
| Heading/namespace agreement | pass |
| Exact literal-namespace schema validation | pass |


[Canonical supplied definition named by heading](../../../../messages/auth.048.001.01/index.md) · [Detailed test evidence and errors](../../../../../../../evidence/archived/434313c645b0c562cbe661e8.md)

The source example is preserved exactly. A valid XML document is not necessarily valid against the schema. A mismatched namespace is not silently updated to the heading version.
