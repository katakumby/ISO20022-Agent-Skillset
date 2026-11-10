---
template: false
document_kind: "source-example"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
message_ids: ["auth.039.001.01"]
literal_namespace: "urn:iso:std:iso:20022:tech:xsd:auth.039.001.01"
source_locations: [{"source_id": "src-000320", "heading_path": ["Business Examples", "Reference Data", "auth.039.001.01"], "heading_paragraph": "P447", "xml_first_paragraph": "P451", "xml_last_paragraph": "P478", "rendered_file_pages": [47, 48]}]
issue_ids: []
limitations: ["Heading and literal namespace remain independent source claims. No example namespace, value or structure has been rewritten."]
---

# Source example — auth.039.001.01

[src-000320](../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md); heading P447; XML P451–P478; Word file pages 47–48.

**P448** Description

**P449** The following MessageInstance provides an example of a Reference Non-working Day message submitted by Tradegate Exchange in relation to segment MIC Tradegate Exchange - Reguliertier Markt.

**P450** Message Instance

## Literal source XML

```xml
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="urn:iso:std:iso:20022:tech:xsd:auth.039.001.01">
	<FinInstrmRptgNonWorkgDayRpt>
		<RptHdr>
			<RptgNtty>
				<MktIdCd>TGAT</MktIdCd>
			</RptgNtty>
			<RptgPrd>
				<FrDtToDt>
					<FrDt>2013-01-01</FrDt>
					<ToDt>2013-12-31</ToDt>
				</FrDtToDt>
			</RptgPrd>
		</RptHdr>
		<NonWorkgDay>
			<Id>
				<MktIdCd>XGRM</MktIdCd>
			</Id>
			<NonWorkgDay>
				<Dt>2013-01-01</Dt>
				<Rsn>PHOL</Rsn>
			</NonWorkgDay>
			<NonWorkgDay>
				<Dt>2013-12-25</Dt>
				<Rsn>PHOL</Rsn>
			</NonWorkgDay>
		</NonWorkgDay>
	</FinInstrmRptgNonWorkgDayRpt>
</Document>
```

## Checks and limitations

| Check | Result |
| --- | --- |
| XML well-formedness | pass |
| Heading definition | auth.039.001.01 |
| Literal namespace | urn:iso:std:iso:20022:tech:xsd:auth.039.001.01 |
| Heading/namespace agreement | pass |
| Exact literal-namespace schema validation | pass |


[Canonical supplied definition named by heading](../../../../messages/auth.039.001.01/index.md) · [Detailed test evidence and errors](../../../../../../../tracking/reviews/fitrr-context-tables-examples.json)

The source example is preserved exactly. A valid XML document is not necessarily valid against the schema. A mismatched namespace is not silently updated to the heading version.
