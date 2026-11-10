---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["Business Examples", "Trading Volume Cap Data", "auth.035.001.01 "]
content_origin: "source-transcription"
---

# auth.035.001.01 

Source: [src-000320](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx). Locator: heading path Business Examples / Trading Volume Cap Data / auth.035.001.01 .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P750** auth.035.001.01 

**P751** Description

**P752** The following MessageInstance provides an example of a Trading Volume Cap message submitted by the Bratislava Stock Exchange.

**P753** Message Instance

**P754** <Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="urn:iso:std:iso:20022:tech:xsd:auth.035.001.01">

**P755** 	<FinInstrmRptgTradgVolCapDataRpt>

**P756** 		<RptHdr>

**P757** 			<RptgNtty>

**P758** 				<MktIdCd>XBRA</MktIdCd>

**P759** 			</RptgNtty>

**P760** 			<RptgPrd>

**P761** 				<FrDtToDt>

**P762** 					<FrDt>2013-06-01</FrDt>

**P763** 					<ToDt>2013-06-15</ToDt>

**P764** 				</FrDtToDt>

**P765** 			</RptgPrd>

**P766** 		</RptHdr>

**P767** 		<VolCapData>

**P768** 			<InstrmRpt>

**P769** 				<TechRcrdId>123ABC</TechRcrdId>

**P770** 				<Id>AB1234567890</Id>

**P771** 				<Ccy>EUR</Ccy>

**P772** 				<TtlTradgVol>10000</TtlTradgVol>

**P773** 				<TtlRefPricTradgVol>500</TtlRefPricTradgVol>

**P774** 				<TtlNgtdTxsTradgVol>750</TtlNgtdTxsTradgVol>

**P775** 			</InstrmRpt>

**P776** 		</VolCapData>

**P777** 	</FinInstrmRptgTradgVolCapDataRpt>

**P778** </Document>

