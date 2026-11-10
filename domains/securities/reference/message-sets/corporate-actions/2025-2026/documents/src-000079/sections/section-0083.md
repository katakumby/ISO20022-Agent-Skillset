---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["Business Examples", "CorporateActionMovementPreliminaryAdvice seev.035.00x.17 – 1"]
content_origin: "source-transcription"
---

# CorporateActionMovementPreliminaryAdvice seev.035.00x.17 – 1

Source: [src-000079](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Locator: heading path Business Examples / CorporateActionMovementPreliminaryAdvice seev.035.00x.17 – 1.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P834** CorporateActionMovementPreliminaryAdvice seev.035.00x.17 – 1

**P835** Description

**P836** This example describes a CorporateActionMovementPreliminaryAdvice sent by an account servicer and containing the final entitlements after the account owner instruction has been accepted.

**P837** The CorporateActionMovementPreliminaryAdvice sample message illustrates a preliminary advice based on the announced event illustrated in the example 1 of the CorporateActionNotification section and based on the instruction illustrated in the example 1 of the CorporateActionInstruction section.

**P838** The corporate action event is a distribution of a dividend to shareholders with a choice of benefit to receive. Shareholders may choose to receive shares, cash.

**P839** Business Data

**P840** Issue name

**P841** Glaxo Holdings

**P842** ISIN GB0007123466

**P843** Terms

**P844** Final dividend of GBP 0,017 per share, OR one ordinary share for every 37 shares held. Elections cannot be made on holdings of less than 37 shares.

**P845** Elections which give rise to fractional entitlements will be rounded down to the nearest whole multiple of 37 shares; the full cash dividend of GBP 0,017 per share will be paid on the remainder of the holding.

**P846** Relative dates

**P847** Ex date - 01 September 2010

**P848** Record date - 07 September 2010

**P849** Dividend payment date - 02 October 2010

**P850** Response deadline date - 23 September 2010

**P851** Transaction description

**P852** A/C 98-0112441-05 has an underlying balance of 80,000 shares.

**P853** Message Instance (with application header)

**P854** <AppHdr xmlns="urn:iso:std:iso:20022:tech:xsd:head.001.001.02" xmlns:n1="http://www.w3.org/2000/09/xmldsig#">

**P855** 	<Fr>

**P856** 		<FIId>

**P857** 			<FinInstnId>

**P858** 				<BICFI>ABCDBEBBXXX</BICFI>

**P859** 			</FinInstnId>

**P860** 		</FIId>

**P861** 	</Fr>

**P862** 	<To>

**P863** 		<FIId>

**P864** 			<FinInstnId>

**P865** 				<BICFI>WXYZFRPP666</BICFI>

**P866** 			</FinInstnId>

**P867** 		</FIId>

**P868** 	</To>

**P869** 	<BizMsgIdr>LOCCUS0000000076</BizMsgIdr>

**P870** 	<MsgDefIdr>seev.035.001.17</MsgDefIdr>

**P871** 	<CreDt>2010-09-15T09:30:00Z</CreDt>

**P872** </AppHdr>

**P873** <Document xmlns="urn:iso:std:iso:20022:tech:xsd:seev.035.001.16" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

**P874** 	<CorpActnMvmntPrlimryAdvc>

**P875** 		<MvmntPrlimryAdvcGnlInf>

**P876** 			<Tp>NEWM</Tp>

**P877** 			<Fctn>CAPA</Fctn>

**P878** 		</MvmntPrlimryAdvcGnlInf>

**P879** 		<NtfctnId>

**P880** 			<Id>LOCCUS0000000001</Id>

**P881** 		</NtfctnId>

**P882** 		<InstrId>

**P883** 			<Id>GLOCUS0000000001</Id>

**P884** 		</InstrId>

**P885** 		<CorpActnGnlInf>

**P886** 			<CorpActnEvtId>DIVGLAX123</CorpActnEvtId>

**P887** 			<OffclCorpActnEvtId>BI01593212345</OffclCorpActnEvtId>

**P888** 			<EvtTp>

**P889** 				<Cd>DVOP</Cd>

**P890** 			</EvtTp>

**P891** 			<MndtryVlntryEvtTp>

**P892** 				<Cd>CHOS</Cd>

**P893** 			</MndtryVlntryEvtTp>

**P894** 			<UndrlygScty>

**P895** 				<FinInstrmId>

**P896** 					<ISIN>GB0007123466</ISIN>

**P897** 					<Desc>GLAXO HOLDINGS</Desc>

**P898** 				</FinInstrmId>

**P899** 			</UndrlygScty>

**P900** 		</CorpActnGnlInf>

**P901** 		<AcctDtls>

**P902** 			<AcctsListAndBalDtls>

**P903** 				<SfkpgAcct>98-0112441-05</SfkpgAcct>

**P904** 				<Bal>

**P905** 					<TtlElgblBal>

**P906** 						<Bal>

**P907** 							<QtyChc>

**P908** 								<SgndQty>

**P909** 									<ShrtLngPos>LONG</ShrtLngPos>

**P910** 									<Qty>

**P911** 										<Unit>80000</Unit>

**P912** 									</Qty>

**P913** 								</SgndQty>

**P914** 							</QtyChc>

**P915** 						</Bal>

**P916** 					</TtlElgblBal>

**P917** 				</Bal>

**P918** 			</AcctsListAndBalDtls>

**P919** 		</AcctDtls>

**P920** 		<CorpActnMvmntDtls>

**P921** 			<OptnNb>002</OptnNb>

**P922** 			<OptnTp>

**P923** 				<Cd>SECU</Cd>

**P924** 			</OptnTp>

**P925** 			<FrctnDspstn>

**P926** 				<Cd>CINL</Cd>

**P927** 			</FrctnDspstn>

**P928** 			<DfltPrcgOrStgInstr>

**P929** 				<DfltOptnInd>false</DfltOptnInd>

**P930** 			</DfltPrcgOrStgInstr>

**P931** 			<DtDtls>

**P932** 				<MktDdln>

**P933** 					<Dt>

**P934** 						<Dt>2010-09-24</Dt>

**P935** 					</Dt>

**P936** 				</MktDdln>

**P937** 				<RspnDdln>

**P938** 					<Dt>

**P939** 						<DtTm>2010-09-23T15:00:00</DtTm>

**P940** 					</Dt>

**P941** 				</RspnDdln>

**P942** 			</DtDtls>

**P943** 			<SctiesMvmntDtls>

**P944** 				<SctyDtls>

**P945** 					<FinInstrmId>

**P946** 						<ISIN>GB0007633421</ISIN>

**P947** 						<Desc>GLAXO WELLCOME</Desc>

**P948** 					</FinInstrmId>

**P949** 				</SctyDtls>

**P950** 				<CdtDbtInd>CRDT</CdtDbtInd>

**P951** 				<EntitldQty>

**P952** 					<Qty>

**P953** 						<Unit>2162</Unit>

**P954** 					</Qty>

**P955** 				</EntitldQty>

**P956** 				<DtDtls>

**P957** 					<PmtDt>

**P958** 						<Dt>2010-10-02</Dt>

**P959** 					</PmtDt>

**P960** 				</DtDtls>

**P961** 				<RateDtls>

**P962** 					<AddtlQtyForExstgScties>

**P963** 						<QtyToQty>

**P964** 							<Qty1>1</Qty1>

**P965** 							<Qty2>37</Qty2>

**P966** 						</QtyToQty>

**P967** 					</AddtlQtyForExstgScties>

**P968** 				</RateDtls>

**P969** 			</SctiesMvmntDtls>

**P970** 			<CshMvmntDtls>

**P971** 				<CdtDbtInd>CRDT</CdtDbtInd>

**P972** 				<AmtDtls>

**P973** 					<CshInLieuOfShr Ccy="GBP">0.10</CshInLieuOfShr>

**P974** 					<EntitldAmt Ccy="GBP">0.10</EntitldAmt>

**P975** 				</AmtDtls>

**P976** 				<DtDtls>

**P977** 					<PmtDt>

**P978** 						<Dt>2010-10-02</Dt>

**P979** 					</PmtDt>

**P980** 					<ValDt>

**P981** 						<Dt>2010-10-02</Dt>

**P982** 					</ValDt>

**P983** 				</DtDtls>

**P984** 			</CshMvmntDtls>

**P985** 		</CorpActnMvmntDtls>

**P986** 	</CorpActnMvmntPrlimryAdvc>

**P987** </Document>

**P988**   


