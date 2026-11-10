---
template: false
document_kind: "source-example"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
message_ids: ["auth.042.001.02"]
literal_namespace: "urn:iso:std:iso:20022:tech:xsd:auth.042.001.02"
source_locations: [{"source_id": "src-000320", "heading_path": ["Business Examples", "Reference Data", "auth.042.001.02"], "heading_paragraph": "P395", "xml_first_paragraph": "P399", "xml_last_paragraph": "P424", "rendered_file_pages": [46, 47]}]
issue_ids: []
limitations: ["Heading and literal namespace remain independent source claims. No example namespace, value or structure has been rewritten."]
---

# Source example — auth.042.001.02

[src-000320](../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx); heading P395; XML P399–P424; Word file pages 46–47.

**P396** Description

**P397** The following MessageInstance provides an example of a Reference Data Invalid message.

**P398** Message Instance

## Literal source XML

```xml
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="urn:iso:std:iso:20022:tech:xsd:auth.042.001.02">
	<FinInstrmRptgInvldRefDataRpt>
		<DtPrd>
			<Dt>2016-01-08</Dt>
		</DtPrd>
		<NbOfRcrds>1</NbOfRcrds>
		<FinInstrms>
			<FinInstrm>
				<FinInstrmGnlAttrbts>
					<Id>AB1234567890</Id>
					<FullNm>InstrumentFullNameHere</FullNm>
					<ShrtNm>HZL ČMB 4,45/10</ShrtNm>
					<ClssfctnTp>ESXXXX</ClssfctnTp>
					<NtnlCcy>EUR</NtnlCcy>
					<CmmdtyDerivInd>false</CmmdtyDerivInd>
				</FinInstrmGnlAttrbts>
				<Issr>EQYXK86SF381Q21S3020</Issr>
				<TradgVnRltdAttrbts>
					<Id>XBUD</Id>
					<IssrReq>false</IssrReq>
					<FrstTradDt>2015-02-23T00:00:00</FrstTradDt>
				</TradgVnRltdAttrbts>
			</FinInstrm>
		</FinInstrms>
	</FinInstrmRptgInvldRefDataRpt>
</Document>
```

## Checks and limitations

| Check | Result |
| --- | --- |
| XML well-formedness | pass |
| Heading definition | auth.042.001.02 |
| Literal namespace | urn:iso:std:iso:20022:tech:xsd:auth.042.001.02 |
| Heading/namespace agreement | pass |
| Exact literal-namespace schema validation | pass |


[Canonical supplied definition named by heading](../../../../messages/auth.042.001.02/index.md) · [Detailed test evidence and errors](../../../../../../../tracking/reviews/fitrr-context-tables-examples.json)

The source example is preserved exactly. A valid XML document is not necessarily valid against the schema. A mismatched namespace is not silently updated to the heading version.
