---
template: false
document_kind: "source-example"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
message_ids: ["auth.040.001.01"]
literal_namespace: "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01"
source_locations: [{"source_id": "src-000320", "heading_path": ["Business Examples", "Transparency Data", "auth.040.001.01 "], "heading_paragraph": "P590", "xml_first_paragraph": "P594", "xml_last_paragraph": "P622", "rendered_file_pages": [51, 52]}]
issue_ids: []
limitations: ["Heading and literal namespace remain independent source claims. No example namespace, value or structure has been rewritten."]
---

# Source example — auth.040.001.01

[src-000320](../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx); heading P590; XML P594–P622; Word file pages 51–52.

**P591** Description

**P592** The following MessageInstance provides an example of a Transparency Equity trading activity message submitted by the Prague Stock Exchange.

**P593** Message Instance

## Literal source XML

```xml
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="urn:iso:std:iso:20022:tech:xsd:auth.040.001.01">
	<FinInstrmRptgEqtyTradgActvtyRpt>
		<RptHdr>
			<RptgNtty>
				<MktIdCd>XPRA</MktIdCd>
			</RptgNtty>
			<RptgPrd>
				<Dt>2013-12-31</Dt>
			</RptgPrd>
		</RptHdr>
		<EqtyTrnsprncyData>
			<TechRcrdId>123ABC</TechRcrdId>
			<Id>AB1234567890</Id>
			<Sspnsn>false</Sspnsn>
			<TxsExctd>
				<Nb>1000</Nb>
				<Vol Ccy="EUR">1500</Vol>
			</TxsExctd>
			<TxsExctdExclgPreTradWvr>
				<Nb>800</Nb>
				<Vol Ccy="EUR">1000</Vol>
			</TxsExctdExclgPreTradWvr>
			<TxsExctdExclgPstTradLrgInScaleWvr>
				<Nb>500</Nb>
				<Vol Ccy="EUR">500</Vol>
			</TxsExctdExclgPstTradLrgInScaleWvr>
		</EqtyTrnsprncyData>
	</FinInstrmRptgEqtyTradgActvtyRpt>
</Document>
```

## Checks and limitations

| Check | Result |
| --- | --- |
| XML well-formedness | pass |
| Heading definition | auth.040.001.01 |
| Literal namespace | urn:iso:std:iso:20022:tech:xsd:auth.040.001.01 |
| Heading/namespace agreement | pass |
| Exact literal-namespace schema validation | pass |


[Canonical supplied definition named by heading](../../../../messages/auth.040.001.01/index.md) · [Detailed test evidence and errors](../../../../../../../tracking/reviews/fitrr-context-tables-examples.json)

The source example is preserved exactly. A valid XML document is not necessarily valid against the schema. A mismatched namespace is not silently updated to the heading version.
