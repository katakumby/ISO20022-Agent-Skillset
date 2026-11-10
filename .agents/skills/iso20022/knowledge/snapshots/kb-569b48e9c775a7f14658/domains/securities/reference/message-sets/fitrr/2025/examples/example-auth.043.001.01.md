---
template: false
document_kind: "source-example"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
message_ids: ["auth.043.001.01"]
literal_namespace: "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01"
source_locations: [{"source_id": "src-000320", "heading_path": ["Business Examples", "Reference Data", "auth.043.001.01"], "heading_paragraph": "P425", "xml_first_paragraph": "P429", "xml_last_paragraph": "P446", "rendered_file_pages": [47]}]
issue_ids: []
limitations: ["Heading and literal namespace remain independent source claims. No example namespace, value or structure has been rewritten."]
---

# Source example — auth.043.001.01

[src-000320](../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md); heading P425; XML P429–P446; Word file pages 47–47.

**P426** Description

**P427** The following MessageInstance provides an example of an Index message that is distributed to various Competent Authorities. It captures an index request that has been made by the United Kingdom Competent Authority on a French index.

**P428** Message Instance

## Literal source XML

```xml
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="urn:iso:std:iso:20022:tech:xsd:auth.043.001.01">
	<FinInstrmRptgRefDataIndxRpt>
		<RptHdr>
			<RptgNtty>
				<NtlCmptntAuthrty>EU</NtlCmptntAuthrty>
			</RptgNtty>
			<RptgPrd>
				<Dt>2013-01-17</Dt>
			</RptgPrd>
		</RptHdr>
		<IndxData>
			<RqstngNtty>GB</RqstngNtty>
			<Indx>
				<ISIN>FR0003500008</ISIN>
			</Indx>
		</IndxData>
	</FinInstrmRptgRefDataIndxRpt>
</Document>
```

## Checks and limitations

| Check | Result |
| --- | --- |
| XML well-formedness | pass |
| Heading definition | auth.043.001.01 |
| Literal namespace | urn:iso:std:iso:20022:tech:xsd:auth.043.001.01 |
| Heading/namespace agreement | pass |
| Exact literal-namespace schema validation | pass |


[Canonical supplied definition named by heading](../../../../messages/auth.043.001.01/index.md) · [Detailed test evidence and errors](../../../../../../../tracking/reviews/fitrr-context-tables-examples.json)

The source example is preserved exactly. A valid XML document is not necessarily valid against the schema. A mismatched namespace is not silently updated to the heading version.
