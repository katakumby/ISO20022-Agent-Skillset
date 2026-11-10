---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["Business Examples", "Reference Data", "auth.017.001.02"]
content_origin: "source-transcription"
---

# auth.017.001.02

Source: [src-000320](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx). Locator: heading path Business Examples / Reference Data / auth.017.001.02.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P256** auth.017.001.02

**P257** Description

**P258** The following MessageInstance provides an example of a Reference Data message that is being reported by the Irish Stock Exchange.

**P259** Message Instance

**P260** <Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="urn:iso:std:iso:20022:tech:xsd:auth.017.001.01">

**P261** 	<FinInstrmRptgRefDataRpt>

**P262** 		<RptHdr>

**P263** 			<RptgNtty>

**P264** 				<MktIdCd>XDUB</MktIdCd>

**P265** 			</RptgNtty>

**P266** 			<RptgPrd>

**P267** 				<Dt>2013-01-17</Dt>

**P268** 			</RptgPrd>

**P269** 			<SubmissnDtTm>2013-01-17T18:05:00</SubmissnDtTm>

**P270** 		</RptHdr>

**P271** 		<RefData>

**P272** 			<TechRcrdId>2015-01-01000120</TechRcrdId>

**P273** 			<FinInstrmGnlAttrbts>

**P274** 				<Id>AB1234567890</Id>

**P275** 				<FullNm>InstrumentFullNameHere</FullNm>

**P276** 				<ShrtNm>HZL ČMB 4,45/10</ShrtNm>

**P277** 				<ClssfctnTp>ESXXXX</ClssfctnTp>

**P278** 				<NtnlCcy>EUR</NtnlCcy>

**P279** 				<CmmdtyDerivInd>false</CmmdtyDerivInd>

**P280** 			</FinInstrmGnlAttrbts>

**P281** 			<Issr>EQYXK86SF381Q21S3020</Issr>

**P282** 			<TradgVnRltdAttrbts>

**P283** 				<Id>XDUB</Id>

**P284** 				<IssrReq>false</IssrReq>

**P285** 				<FrstTradDt>2015-02-23T00:00:00</FrstTradDt>

**P286** 			</TradgVnRltdAttrbts>

**P287** 		</RefData>

**P288** 		<RefData>

**P289** 			<TechRcrdId>2015-01-01000121</TechRcrdId>

**P290** 			<FinInstrmGnlAttrbts>

**P291** 				<Id>AB1234567890</Id>

**P292** 				<FullNm>InstrumentFullNameHere </FullNm>

**P293** 				<ShrtNm>HZL ČMB 4,45/10</ShrtNm>

**P294** 				<ClssfctnTp>DBVQFX</ClssfctnTp>

**P295** 				<NtnlCcy>EUR</NtnlCcy>

**P296** 				<CmmdtyDerivInd>false</CmmdtyDerivInd>

**P297** 			</FinInstrmGnlAttrbts>

**P298** 			<Issr>EQYXK86SF381Q21S3020</Issr>

**P299** 			<TradgVnRltdAttrbts>

**P300** 				<Id>XHEL</Id>

**P301** 				<IssrReq>false</IssrReq>

**P302** 				<FrstTradDt>2015-02-23T00:00:00</FrstTradDt>

**P303** 			</TradgVnRltdAttrbts>

**P304** 			<DebtInstrmAttrbts>

**P305** 				<TtlIssdNmnlAmt Ccy="CZK">349.60937</TtlIssdNmnlAmt>

**P306** 				<MtrtyDt>2010-05-19</MtrtyDt>

**P307** 				<NmnlValPerUnit Ccy="CZK">100.0</NmnlValPerUnit>

**P308** 				<IntrstRate>

**P309** 					<Fltg>

**P310** 						<RefRate>

**P311** 							<ISIN>PN5QWZKIH3L9</ISIN>

**P312** 						</RefRate>

**P313** 						<Term>

**P314** 							<Unit>MNTH</Unit>

**P315** 							<Val>232</Val>

**P316** 						</Term>

**P317** 						<BsisPtSprd>14300</BsisPtSprd>

**P318** 					</Fltg>

**P319** 				</IntrstRate>

**P320** 				<DebtSnrty>JUND</DebtSnrty>

**P321** 			</DebtInstrmAttrbts>

**P322** 		</RefData>

**P323** 		<RefData>

**P324** 			<TechRcrdId>2015-01-01000122</TechRcrdId>

**P325** 			<FinInstrmGnlAttrbts>

**P326** 				<Id>AB1234567890</Id>

**P327** 				<FullNm>InstrumentFullNameHere </FullNm>

**P328** 				<ShrtNm>DAX9908TLOPENZ</ShrtNm>

**P329** 				<ClssfctnTp>FFFPXX</ClssfctnTp>

**P330** 				<NtnlCcy>EUR</NtnlCcy>

**P331** 				<CmmdtyDerivInd>false</CmmdtyDerivInd>

**P332** 			</FinInstrmGnlAttrbts>

**P333** 			<Issr>885100KZRBC1KP0WDC71</Issr>

**P334** 			<TradgVnRltdAttrbts>

**P335** 				<Id>XLIS</Id>

**P336** 				<IssrReq>false</IssrReq>

**P337** 				<FrstTradDt>2015-02-23T00:00:00</FrstTradDt>

**P338** 			</TradgVnRltdAttrbts>

**P339** 			<DerivInstrmAttrbts>

**P340** 				<XpryDt>2015-02-28</XpryDt>

**P341** 				<PricMltplr>60.9</PricMltplr>

**P342** 				<UndrlygInstrm>

**P343** 					<Sngl>

**P344** 						<ISIN>AJSQW9HOSNR8</ISIN>

**P345** 					</Sngl>

**P346** 				</UndrlygInstrm>

**P347** 				<DlvryTp>PHYS</DlvryTp>

**P348** 				<AsstClssSpcfcAttrbts>

**P349** 					<FX>

**P350** 						<FxTp>FXEM</FxTp>

**P351** 						<OthrNtnlCcy>GHS</OthrNtnlCcy>

**P352** 					</FX>

**P353** 				</AsstClssSpcfcAttrbts>

**P354** 			</DerivInstrmAttrbts>

**P355** 		</RefData>

**P356** 	</FinInstrmRptgRefDataRpt>

**P357** </Document>

