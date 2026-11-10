---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["Business Examples", "Transparency Data", "auth.040.001.01 "]
content_origin: "source-transcription"
---

# auth.040.001.01 

Source: [src-000320](../../../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md). Locator: heading path Business Examples / Transparency Data / auth.040.001.01 .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P590** auth.040.001.01 

**P591** Description

**P592** The following MessageInstance provides an example of a Transparency Equity trading activity message submitted by the Prague Stock Exchange.

**P593** Message Instance

**P594** <Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="urn:iso:std:iso:20022:tech:xsd:auth.040.001.01">

**P595** 	<FinInstrmRptgEqtyTradgActvtyRpt>

**P596** 		<RptHdr>

**P597** 			<RptgNtty>

**P598** 				<MktIdCd>XPRA</MktIdCd>

**P599** 			</RptgNtty>

**P600** 			<RptgPrd>

**P601** 				<Dt>2013-12-31</Dt>

**P602** 			</RptgPrd>

**P603** 		</RptHdr>

**P604** 		<EqtyTrnsprncyData>

**P605** 			<TechRcrdId>123ABC</TechRcrdId>

**P606** 			<Id>AB1234567890</Id>

**P607** 			<Sspnsn>false</Sspnsn>

**P608** 			<TxsExctd>

**P609** 				<Nb>1000</Nb>

**P610** 				<Vol Ccy="EUR">1500</Vol>

**P611** 			</TxsExctd>

**P612** 			<TxsExctdExclgPreTradWvr>

**P613** 				<Nb>800</Nb>

**P614** 				<Vol Ccy="EUR">1000</Vol>

**P615** 			</TxsExctdExclgPreTradWvr>

**P616** 			<TxsExctdExclgPstTradLrgInScaleWvr>

**P617** 				<Nb>500</Nb>

**P618** 				<Vol Ccy="EUR">500</Vol>

**P619** 			</TxsExctdExclgPstTradLrgInScaleWvr>

**P620** 		</EqtyTrnsprncyData>

**P621** 	</FinInstrmRptgEqtyTradgActvtyRpt>

**P622** </Document>

