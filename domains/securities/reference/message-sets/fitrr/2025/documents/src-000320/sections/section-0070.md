---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["Business Examples", "Reference Data", "auth.039.001.01"]
content_origin: "source-transcription"
---

# auth.039.001.01

Source: [src-000320](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx). Locator: heading path Business Examples / Reference Data / auth.039.001.01.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P447** auth.039.001.01

**P448** Description

**P449** The following MessageInstance provides an example of a Reference Non-working Day message submitted by Tradegate Exchange in relation to segment MIC Tradegate Exchange - Reguliertier Markt.

**P450** Message Instance

**P451** <Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="urn:iso:std:iso:20022:tech:xsd:auth.039.001.01">

**P452** 	<FinInstrmRptgNonWorkgDayRpt>

**P453** 		<RptHdr>

**P454** 			<RptgNtty>

**P455** 				<MktIdCd>TGAT</MktIdCd>

**P456** 			</RptgNtty>

**P457** 			<RptgPrd>

**P458** 				<FrDtToDt>

**P459** 					<FrDt>2013-01-01</FrDt>

**P460** 					<ToDt>2013-12-31</ToDt>

**P461** 				</FrDtToDt>

**P462** 			</RptgPrd>

**P463** 		</RptHdr>

**P464** 		<NonWorkgDay>

**P465** 			<Id>

**P466** 				<MktIdCd>XGRM</MktIdCd>

**P467** 			</Id>

**P468** 			<NonWorkgDay>

**P469** 				<Dt>2013-01-01</Dt>

**P470** 				<Rsn>PHOL</Rsn>

**P471** 			</NonWorkgDay>

**P472** 			<NonWorkgDay>

**P473** 				<Dt>2013-12-25</Dt>

**P474** 				<Rsn>PHOL</Rsn>

**P475** 			</NonWorkgDay>

**P476** 		</NonWorkgDay>

**P477** 	</FinInstrmRptgNonWorkgDayRpt>

**P478** </Document>

