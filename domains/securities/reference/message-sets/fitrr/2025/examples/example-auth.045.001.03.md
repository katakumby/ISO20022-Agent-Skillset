---
template: false
document_kind: "source-example"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
message_ids: ["auth.045.001.03"]
literal_namespace: "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03"
source_locations: [{"source_id": "src-000320", "heading_path": ["Business Examples", "Transparency Data", "auth.045.001.03 "], "heading_paragraph": "P712", "xml_first_paragraph": "P716", "xml_last_paragraph": "P748", "rendered_file_pages": [55]}]
issue_ids: ["issue-000055"]
limitations: ["Heading and literal namespace remain independent source claims. No example namespace, value or structure has been rewritten."]
---

# Source example — auth.045.001.03

[src-000320](../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx); heading P712; XML P716–P748; Word file pages 55–55.

**P713** Description

**P714** The following MessageInstance provides an example of a Transparency Non-Equity trading activity result message submitted by the Bulgarian National Competent Authority.

**P715** Message Instance

## Literal source XML

```xml
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="urn:iso:std:iso:20022:tech:xsd:auth.045.001.03">
	<FinInstrmRptgNonEqtyTradgActvtyRslt>
		<RptHdr>
			<RptgNtty>
				<NtlCmptntAuthrty>BG</NtlCmptntAuthrty>
			</RptgNtty>
			<RptgPrd>
				<Dt>2013-12-31</Dt>
			</RptgPrd>
		</RptHdr>
		<NonEqtyTrnsprncyData>
			<TechRcrdId>123ABC</TechRcrdId>
			<Id>AB1234567890</Id>
			<Lqdty>true</Lqdty>
			<PreTradLrgInScaleThrshld>
				<Nb>10000</Nb>
			</PreTradLrgInScaleThrshld>
			<PstTradLrgInScaleThrshld>
				<Nb>10000</Nb>
			</PstTradLrgInScaleThrshld>
			<PreTradInstrmSzSpcfcThrshld>
				<Nb>10000</Nb>
			</PreTradInstrmSzSpcfcThrshld>
			<PstTradInstrmSzSpcfcThrshld>
				<Nb>10000</Nb>
			</PstTradInstrmSzSpcfcThrshld>
			<Sttstcs>
				<TtlNbOfTxsExctd>10000</TtlNbOfTxsExctd>
				<TtlVolOfTxsExctd>10000</TtlVolOfTxsExctd>
			</Sttstcs>
		</NonEqtyTrnsprncyData>
	</FinInstrmRptgNonEqtyTradgActvtyRslt>
</Document>
```

## Checks and limitations

| Check | Result |
| --- | --- |
| XML well-formedness | pass |
| Heading definition | auth.045.001.03 |
| Literal namespace | urn:iso:std:iso:20022:tech:xsd:auth.045.001.03 |
| Heading/namespace agreement | pass |
| Exact literal-namespace schema validation | fail |


[Canonical supplied definition named by heading](../../../../messages/auth.045.001.03/index.md) · [Detailed test evidence and errors](../../../../../../../tracking/reviews/fitrr-context-tables-examples.json)

The source example is preserved exactly. A valid XML document is not necessarily valid against the schema. A mismatched namespace is not silently updated to the heading version.
