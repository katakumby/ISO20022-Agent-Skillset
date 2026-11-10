---
template: false
document_kind: "source-example"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
message_ids: ["auth.032.001.01"]
literal_namespace: "urn:iso:std:iso:20022:tech:xsd:auth.032.001.01"
source_locations: [{"source_id": "src-000320", "heading_path": ["Business Examples", "Transparency Data", "auth.032.001.01 "], "heading_paragraph": "P567", "xml_first_paragraph": "P571", "xml_last_paragraph": "P589", "rendered_file_pages": [51]}]
issue_ids: ["issue-000055"]
limitations: ["Heading and literal namespace remain independent source claims. No example namespace, value or structure has been rewritten."]
---

# Source example — auth.032.001.01

[src-000320](../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx); heading P567; XML P571–P589; Word file pages 51–51.

**P568** Description

**P569** The following MessageInstance provides an example of a Transparency Equity message submitted by the Luxembourg Stock Exchange

**P570** Message Instance

## Literal source XML

```xml
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="urn:iso:std:iso:20022:tech:xsd:auth.032.001.01">
	<FinInstrmRptgEqtyTrnsprncyDataRpt>
		<RptHdr>
			<RptgNtty>
				<MktIdCd>XLUX</MktIdCd>
			</RptgNtty>
			<RptgPrd>
				<Dt>2013-12-31</Dt>
			</RptgPrd>
		</RptHdr>
		<EqtyTrnsprncyData>
			<TechRcrdId>123ABC</TechRcrdId>
			<Id>AB1234567890</Id>
			<FinInstrmClssfctn>SHRS</FinInstrmClssfctn>
			<NbInstrm>10</NbInstrm>
			<NbOutsdngShrs>5</NbOutsdngShrs>
		</EqtyTrnsprncyData>
	</FinInstrmRptgEqtyTrnsprncyDataRpt>
</Document>
```

## Checks and limitations

| Check | Result |
| --- | --- |
| XML well-formedness | pass |
| Heading definition | auth.032.001.01 |
| Literal namespace | urn:iso:std:iso:20022:tech:xsd:auth.032.001.01 |
| Heading/namespace agreement | pass |
| Exact literal-namespace schema validation | fail |


[Canonical supplied definition named by heading](../../../../messages/auth.032.001.01/index.md) · [Detailed test evidence and errors](../../../../../../../tracking/reviews/fitrr-context-tables-examples.json)

The source example is preserved exactly. A valid XML document is not necessarily valid against the schema. A mismatched namespace is not silently updated to the heading version.
