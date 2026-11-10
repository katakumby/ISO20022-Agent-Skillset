---
template: false
document_kind: "source-example"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
message_ids: ["auth.049.001.02"]
literal_namespace: "urn:iso:std:iso:20022:tech:xsd:auth.049.001.01"
source_locations: [{"source_id": "src-000320", "heading_path": ["Business Examples", "Reference Data", "auth.049.001.02"], "heading_paragraph": "P524", "xml_first_paragraph": "P528", "xml_last_paragraph": "P550", "rendered_file_pages": [50]}]
issue_ids: ["issue-000055"]
limitations: ["Heading and literal namespace remain independent source claims. No example namespace, value or structure has been rewritten."]
---

# Source example — auth.049.001.02

[src-000320](../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx); heading P524; XML P528–P550; Word file pages 50–50.

**P525** Description

**P526** The following MessageInstance provides an example of the Reference Market Identification Code message that is distributed to Competent Authorities.

**P527** Message Instance

## Literal source XML

```xml
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="urn:iso:std:iso:20022:tech:xsd:auth.049.001.01">
	<FinInstrmRptgMktIdCdRpt>
		<MktId>
			<Oprg>XWBO</Oprg>
			<Sgmt>WBGF</Sgmt>
			<Tp>SGMT</Tp>
			<Ctgy>RMKT</Ctgy>
			<InstnNm>VenueNameHere</InstnNm>
			<City>CityNameHere</City>
			<Ctry>
				<Cd>AT</Cd>
			</Ctry>
			<AuthrtyNm>AuthorityNameHere</AuthrtyNm>
			<Mod>NOCH</Mod>
			<CreDt>2007-07-01</CreDt>
			<VldtyPrd>
				<FrDt>2007-07-01</FrDt>
			</VldtyPrd>
			<StsDt>2015-02-01</StsDt>
			<LastUpdtdDt>2007-07-01T03:00:13</LastUpdtdDt>
		</MktId>
	</FinInstrmRptgMktIdCdRpt>
</Document>
```

## Checks and limitations

| Check | Result |
| --- | --- |
| XML well-formedness | pass |
| Heading definition | auth.049.001.02 |
| Literal namespace | urn:iso:std:iso:20022:tech:xsd:auth.049.001.01 |
| Heading/namespace agreement | fail |
| Exact literal-namespace schema validation | not-run |


[Canonical supplied definition named by heading](../../../../messages/auth.049.001.02/index.md) · [Detailed test evidence and errors](../../../../../../../tracking/reviews/fitrr-context-tables-examples.json)

The source example is preserved exactly. A valid XML document is not necessarily valid against the schema. A mismatched namespace is not silently updated to the heading version.
