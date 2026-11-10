---
template: false
document_kind: "source-example"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
message_ids: ["auth.044.001.03"]
literal_namespace: "urn:iso:std:iso:20022:tech:xsd:auth.044.001.02"
source_locations: [{"source_id": "src-000320", "heading_path": ["Business Examples", "Transparency Data", "auth.044.001.03 "], "heading_paragraph": "P623", "xml_first_paragraph": "P627", "xml_last_paragraph": "P648", "rendered_file_pages": [52, 53]}]
issue_ids: ["issue-000055"]
limitations: ["Heading and literal namespace remain independent source claims. No example namespace, value or structure has been rewritten."]
---

# Source example — auth.044.001.03

[src-000320](../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx); heading P623; XML P627–P648; Word file pages 52–53.

**P624** Description

**P625** The following MessageInstance provides an example of a Transparency Equity trading activity result message submitted by the Polish National Competent Authority.

**P626** Message Instance

## Literal source XML

```xml
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="urn:iso:std:iso:20022:tech:xsd:auth.044.001.02">
	<FinInstrmRptgEqtyTradgActvtyRslt>
		<RptHdr>
			<RptgNtty>
				<NtlCmptntAuthrty>PL</NtlCmptntAuthrty>
			</RptgNtty>
			<RptgPrd>
				<Dt>2013-12-31</Dt>
			</RptgPrd>
		</RptHdr>
		<EqtyTrnsprncyData>
			<TechRcrdId>123ABC</TechRcrdId>
			<Id>AB1234567890</Id>
			<Lqdty>true</Lqdty>
			<Mthdlgy>ESTM</Mthdlgy>
			<Sttstcs>
				<AvrgDalyTrnvr Ccy="PLN">10000</AvrgDalyTrnvr>
				<AvrgTxVal Ccy="PLN">10000</AvrgTxVal>
			</Sttstcs>
		</EqtyTrnsprncyData>
	</FinInstrmRptgEqtyTradgActvtyRslt>
</Document>
```

## Checks and limitations

| Check | Result |
| --- | --- |
| XML well-formedness | pass |
| Heading definition | auth.044.001.03 |
| Literal namespace | urn:iso:std:iso:20022:tech:xsd:auth.044.001.02 |
| Heading/namespace agreement | fail |
| Exact literal-namespace schema validation | not-run |


[Canonical supplied definition named by heading](../../../../messages/auth.044.001.03/index.md) · [Detailed test evidence and errors](../../../../../../../tracking/reviews/fitrr-context-tables-examples.json)

The source example is preserved exactly. A valid XML document is not necessarily valid against the schema. A mismatched namespace is not silently updated to the heading version.
