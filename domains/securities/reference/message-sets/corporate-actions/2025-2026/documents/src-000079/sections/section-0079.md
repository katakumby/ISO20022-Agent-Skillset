---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["Business Examples", "CorporateActionNotification seev.031.00x.16"]
content_origin: "source-transcription"
---

# CorporateActionNotification seev.031.00x.16

Source: [src-000079](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Locator: heading path Business Examples / CorporateActionNotification seev.031.00x.16.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P405** CorporateActionNotification seev.031.00x.16

**P406** Description

**P407** This example describes a CorporateActionNotification sent by an account servicer containing the initial announcement of a dividend option event for which the event details are complete, the event is confirmed and the eligible balance provided. 

**P408** The corporate action event is a distribution of a dividend to shareholders with a choice of benefit to receive. Shareholders may choose to receive shares, cash. To be distinguished from DRIP as the company creates new share capital in exchange for the dividend rather than investing the dividend in the market.

**P409** Business Data

**P410** Issue name

**P411** Glaxo Holdings

**P412** ISIN GB0007123466

**P413** Terms

**P414** Final dividend of GBP 0,017 per share, OR one ordinary share for every 37 shares held. Elections cannot be made on holdings of less than 37 shares.

**P415** Elections which give rise to fractional entitlements will be rounded down to the nearest whole multiple of 37 shares; the full cash dividend of GBP 0,017 per share will be paid on the remainder of the holding.

**P416** Relative dates

**P417** Ex date - 01 September 2010

**P418** Record date - 07 September 2010

**P419** Dividend payment date - 02 October 2010

**P420** Response deadline date - 23 September 2010

**P421** Transaction description

**P422** A/C 98-0112441-05 has an underlying balance of 80.000 shares.

**P423** Message Instance (with application header)

**P424** <AppHdr xmlns="urn:iso:std:iso:20022:tech:xsd:head.001.001.02" xmlns:n1="http://www.w3.org/2000/09/xmldsig#">

**P425** 	<Fr>

**P426** 		<FIId>

**P427** 			<FinInstnId>

**P428** 				<BICFI>ABCDBEBBXXX</BICFI>

**P429** 			</FinInstnId>

**P430** 		</FIId>

**P431** 	</Fr>

**P432** 	<To>

**P433** 		<FIId>

**P434** 			<FinInstnId>

**P435** 				<BICFI>WXYZFRPP666</BICFI>

**P436** 			</FinInstnId>

**P437** 		</FIId>

**P438** 	</To>

**P439** 	<BizMsgIdr>LOCCUS000000001</BizMsgIdr>

**P440** 	<MsgDefIdr>seev.031.001.16</MsgDefIdr>

**P441** 	<CreDt>2010-08-15T09:30:00Z</CreDt>

**P442** </AppHdr>

**P443** <Document xmlns="urn:iso:std:iso:20022:tech:xsd:seev.031.001.16" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

**P444** 	<CorpActnNtfctn>

**P445** 		<NtfctnGnlInf>

**P446** 			<NtfctnTp>NEWM</NtfctnTp>

**P447** 			<PrcgSts>

**P448** 				<Cd>

**P449** 					<EvtCmpltnsSts>COMP</EvtCmpltnsSts>

**P450** 					<EvtConfSts>CONF</EvtConfSts>

**P451** 				</Cd>

**P452** 			</PrcgSts>

**P453** 		</NtfctnGnlInf>

**P454** 		<CorpActnGnlInf>

**P455** 			<CorpActnEvtId>DIVGLAX123</CorpActnEvtId>

**P456** 			<OffclCorpActnEvtId>BI01593212345</OffclCorpActnEvtId>

**P457** 			<EvtTp>

**P458** 				<Cd>DVOP</Cd>

**P459** 			</EvtTp>

**P460** 			<MndtryVlntryEvtTp>

**P461** 				<Cd>CHOS</Cd>

**P462** 			</MndtryVlntryEvtTp>

**P463** 			<UndrlygScty>

**P464** 				<FinInstrmId>

**P465** 					<ISIN>GB0007123466</ISIN>

**P466** 					<Desc>GLAXO HOLDINGS</Desc>

**P467** 				</FinInstrmId>

**P468** 			</UndrlygScty>

**P469** 		</CorpActnGnlInf>

**P470** 		<AcctDtls>

**P471** 			<AcctsListAndBalDtls>

**P472** 				<SfkpgAcct>98-0112441-05</SfkpgAcct>

**P473** 				<Bal>

**P474** 					<TtlElgblBal>

**P475** 						<Bal>

**P476** 							<QtyChc>

**P477** 								<SgndQty>

**P478** 									<ShrtLngPos>LONG</ShrtLngPos>

**P479** 									<Qty>

**P480** 										<Unit>80000</Unit>

**P481** 									</Qty>

**P482** 								</SgndQty>

**P483** 							</QtyChc>

**P484** 						</Bal>

**P485** 					</TtlElgblBal>

**P486** 				</Bal>

**P487** 			</AcctsListAndBalDtls>

**P488** 		</AcctDtls>

**P489** 		<CorpActnDtls>

**P490** 			<DtDtls>

**P491** 				<RcrdDt>

**P492** 					<Dt>2010-09-07</Dt>

**P493** 				</RcrdDt>

**P494** 				<ExDvddDt>

**P495** 					<Dt>2010-09-01</Dt>

**P496** 				</ExDvddDt>

**P497** 			</DtDtls>

**P498** 			<ShrhldrRghtsDrctvInd>true</ShrhldrRghtsDrctvInd>

**P499** 			<DvddTp>

**P500** 				<Cd>FINL</Cd>

**P501** 			</DvddTp>

**P502** 		</CorpActnDtls>

**P503** 		<CorpActnOptnDtls>

**P504** 			<OptnNb>001</OptnNb>

**P505** 			<OptnTp>

**P506** 				<Cd>CASH</Cd>

**P507** 			</OptnTp>

**P508** 			<DfltPrcgOrStgInstr>

**P509** 				<DfltOptnInd>true</DfltOptnInd>

**P510** 			</DfltPrcgOrStgInstr>

**P511** 			<DtDtls>

**P512** 				<MktDdln>

**P513** 					<Dt>

**P514** 						<Dt>2010-09-24</Dt>

**P515** 					</Dt>

**P516** 				</MktDdln>

**P517** 				<RspnDdln>

**P518** 					<Dt>

**P519** 						<DtTm>2010-09-23T15:00:00</DtTm>

**P520** 					</Dt>

**P521** 				</RspnDdln>

**P522** 			</DtDtls>

**P523** 			<RateAndAmtDtls>

**P524** 			<GrssDstrbtnRate>

**P525** 					<Amt Ccy="GBP">0.017</Amt>

**P526** 			</GrssDstrbtnRate>

**P527** 			</RateAndAmtDtls>

**P528** 			<CshMvmntDtls>

**P529** 				<CdtDbtInd>CRDT</CdtDbtInd>

**P530** 				<DtDtls>

**P531** 					<PmtDt>

**P532** 						<Dt>2009-10-02</Dt>

**P533** 					</PmtDt>

**P534** 				</DtDtls>

**P535** 			</CshMvmntDtls>

**P536** 		</CorpActnOptnDtls>

**P537** 		<CorpActnOptnDtls>

**P538** 			<OptnNb>002</OptnNb>

**P539** 			<OptnTp>

**P540** 				<Cd>SECU</Cd>

**P541** 			</OptnTp>

**P542** 			<FrctnDspstn>

**P543** 				<Cd>CINL</Cd>

**P544** 			</FrctnDspstn>

**P545** 			<DfltPrcgOrStgInstr>

**P546** 				<DfltOptnInd>false</DfltOptnInd>

**P547** 			</DfltPrcgOrStgInstr>

**P548** 			<FinInstrmId>

**P549** 				<ISIN>GB0007633421</ISIN>

**P550** 				<Desc>GLAXO WELLCOME</Desc>

**P551** 			</FinInstrmId>

**P552** 			<DtDtls>

**P553** 				<MktDdln>

**P554** 					<Dt>

**P555** 						<Dt>2010-09-24</Dt>

**P556** 					</Dt>

**P557** 				</MktDdln>

**P558** 				<RspnDdln>

**P559** 					<Dt>

**P560** 						<DtTm>2010-09-23T15:00:00</DtTm>

**P561** 					</Dt>

**P562** 				</RspnDdln>

**P563** 			</DtDtls>

**P564** 			<SctiesMvmntDtls>

**P565** 				<SctyDtls>

**P566** 					<FinInstrmId>

**P567** 						<ISIN>GB0007633421</ISIN>

**P568** 						<Desc>GLAXO WELLCOME</Desc>

**P569** 					</FinInstrmId>

**P570** 				</SctyDtls>

**P571** 				<CdtDbtInd>CRDT</CdtDbtInd>

**P572** 				<EntitldQty>

**P573** 					<Qty>

**P574** 						<Unit>2162</Unit>

**P575** 					</Qty>

**P576** 				</EntitldQty>

**P577** 				<DtDtls>

**P578** 					<PmtDt>

**P579** 						<Dt>2010-10-02</Dt>

**P580** 					</PmtDt>

**P581** 				</DtDtls>

**P582** 				<RateDtls>

**P583** 					<AddtlQtyForExstgScties>

**P584** 						<QtyToQty>

**P585** 							<Qty1>1</Qty1>

**P586** 							<Qty2>37</Qty2>

**P587** 						</QtyToQty>

**P588** 					</AddtlQtyForExstgScties>

**P589** 				</RateDtls>

**P590** 			</SctiesMvmntDtls>

**P591** 		</CorpActnOptnDtls>

**P592** 	</CorpActnNtfctn>

**P593** </Document>

