---
template: false
document_kind: "source-example"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
message_ids: ["auth.035.001.01"]
literal_namespace: "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01"
source_locations: [{"source_id": "src-000320", "heading_path": ["Business Examples", "Trading Volume Cap Data", "auth.035.001.01 "], "heading_paragraph": "P750", "xml_first_paragraph": "P754", "xml_last_paragraph": "P778", "rendered_file_pages": [56]}]
issue_ids: []
limitations: ["Heading and literal namespace remain independent source claims. No example namespace, value or structure has been rewritten."]
---

# Source example — auth.035.001.01

[src-000320](../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md); heading P750; XML P754–P778; Word file pages 56–56.

**P751** Description

**P752** The following MessageInstance provides an example of a Trading Volume Cap message submitted by the Bratislava Stock Exchange.

**P753** Message Instance

## Literal source XML

```xml
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="urn:iso:std:iso:20022:tech:xsd:auth.035.001.01">
	<FinInstrmRptgTradgVolCapDataRpt>
		<RptHdr>
			<RptgNtty>
				<MktIdCd>XBRA</MktIdCd>
			</RptgNtty>
			<RptgPrd>
				<FrDtToDt>
					<FrDt>2013-06-01</FrDt>
					<ToDt>2013-06-15</ToDt>
				</FrDtToDt>
			</RptgPrd>
		</RptHdr>
		<VolCapData>
			<InstrmRpt>
				<TechRcrdId>123ABC</TechRcrdId>
				<Id>AB1234567890</Id>
				<Ccy>EUR</Ccy>
				<TtlTradgVol>10000</TtlTradgVol>
				<TtlRefPricTradgVol>500</TtlRefPricTradgVol>
				<TtlNgtdTxsTradgVol>750</TtlNgtdTxsTradgVol>
			</InstrmRpt>
		</VolCapData>
	</FinInstrmRptgTradgVolCapDataRpt>
</Document>
```

## Checks and limitations

| Check | Result |
| --- | --- |
| XML well-formedness | pass |
| Heading definition | auth.035.001.01 |
| Literal namespace | urn:iso:std:iso:20022:tech:xsd:auth.035.001.01 |
| Heading/namespace agreement | pass |
| Exact literal-namespace schema validation | pass |


[Canonical supplied definition named by heading](../../../../messages/auth.035.001.01/index.md) · [Detailed test evidence and errors](../../../../../../../evidence/archived/434313c645b0c562cbe661e8.md)

The source example is preserved exactly. A valid XML document is not necessarily valid against the schema. A mismatched namespace is not silently updated to the heading version.
