---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["Business Examples", "Transparency Data", "auth.041.001.01 "]
content_origin: "source-transcription"
---

# auth.041.001.01 

Source: [src-000320](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx). Locator: heading path Business Examples / Transparency Data / auth.041.001.01 .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P674** auth.041.001.01 

**P675** Description

**P676** The following MessageInstance provides an example of a Transparency Non-Equity trading activity message submitted by the Athens Stock Exchange.

**P677** Message Instance

**P678** <Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="urn:iso:std:iso:20022:tech:xsd:auth.041.001.01">

**P679** 	<FinInstrmRptgNonEqtyTradgActvtyRpt>

**P680** 		<RptHdr>

**P681** 			<RptgNtty>

**P682** 				<MktIdCd>ASEX</MktIdCd>

**P683** 			</RptgNtty>

**P684** 			<RptgPrd>

**P685** 				<Dt>2013-12-31</Dt>

**P686** 			</RptgPrd>

**P687** 		</RptHdr>

**P688** 		<NonEqtyTrnsprncyData>

**P689** 			<TechRcrdId>123ABC</TechRcrdId>

**P690** 			<Id>AB1234567890</Id>

**P691** 			<Sspnsn>false</Sspnsn>

**P692** 			<NbTxs>100</NbTxs>

**P693** 			<AggtdQttvData>

**P694** 				<NbOfTxs>40</NbOfTxs>

**P695** 				<TtlNtnlAmt>1000</TtlNtnlAmt>

**P696** 				<Rg>

**P697** 					<FrQty>0</FrQty>

**P698** 					<ToQty>100000</ToQty>

**P699** 				</Rg>

**P700** 			</AggtdQttvData>

**P701** 			<AggtdQttvData>

**P702** 				<NbOfTxs>60</NbOfTxs>

**P703** 				<TtlNtnlAmt>1000</TtlNtnlAmt>

**P704** 				<Rg>

**P705** 					<FrQty>100000</FrQty>

**P706** 					<ToQty>200000</ToQty>

**P707** 				</Rg>

**P708** 			</AggtdQttvData>

**P709** 		</NonEqtyTrnsprncyData>

**P710** 	</FinInstrmRptgNonEqtyTradgActvtyRpt>

**P711** </Document>

