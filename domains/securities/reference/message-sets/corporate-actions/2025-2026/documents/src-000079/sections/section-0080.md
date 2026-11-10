---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["Business Examples", "CorporateActionEventProcessingStatusAdvice seev.032.00x.09"]
content_origin: "source-transcription"
---

# CorporateActionEventProcessingStatusAdvice seev.032.00x.09

Source: [src-000079](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Locator: heading path Business Examples / CorporateActionEventProcessingStatusAdvice seev.032.00x.09.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P594** CorporateActionEventProcessingStatusAdvice seev.032.00x.09

**P595** Description

**P596** This example describes a CorporateActionEventProcessingStatusAdvice sent by an account servicer after the payment date after having sent already a CorporateActionMovementPreliminaryAdvice message. The event processing status advice informs the account owner that the processing of the corporate action event is pending because the securities have not been delivered by the issuer.

**P597** The message refers to the previously sent notification and movement preliminary advice that are illustrated in the examples of the related messages (seev.031 and seev.035). The corporate action event is a distribution of a dividend to shareholders with a choice of benefit to receive. Shareholders may choose to receive shares, cash.

**P598** Business Data

**P599** Issue name

**P600** Glaxo Holdings

**P601** ISIN GB0007123466

**P602** Terms

**P603** Final dividend of GBP 0,017 per share, OR one ordinary share for every 37 shares held. Elections cannot be made on holdings of less than 37 shares.

**P604** Elections which give rise to fractional entitlements will be rounded down to the nearest whole multiple of 37 shares; the full cash dividend of GBP 0,017 per share will be paid on the remainder of the holding.

**P605** Relative dates

**P606** Ex date - 01 September 2010

**P607** Record date - 07 September 2010

**P608** Dividend payment date - 02 October 2010

**P609** Response deadline date - 23 September 2010

**P610** Transaction description

**P611** A/C 98-0112441-05 has an underlying balance of 80.000 shares.

**P612** Message Instance (with application header)

**P613** <AppHdr xmlns="urn:iso:std:iso:20022:tech:xsd:head.001.001.02" xmlns:n1="http://www.w3.org/2000/09/xmldsig#">

**P614** 	<Fr>

**P615** 		<FIId>

**P616** 			<FinInstnId>

**P617** 				<BICFI>ABCDBEBBXXX</BICFI>

**P618** 			</FinInstnId>

**P619** 		</FIId>

**P620** 	</Fr>

**P621** 	<To>

**P622** 		<FIId>

**P623** 			<FinInstnId>

**P624** 				<BICFI>WXYZFRPP666</BICFI>

**P625** 			</FinInstnId>

**P626** 		</FIId>

**P627** 	</To>

**P628** 	<BizMsgIdr>LOCCUS0000000035</BizMsgIdr>

**P629** 	<MsgDefIdr>seev.032.001.09</MsgDefIdr>

**P630** 	<CreDt>2010-10-03T09:30:00Z</CreDt>

**P631** </AppHdr>

**P632** <Document xmlns="urn:iso:std:iso:20022:tech:xsd:seev.032.001.09" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

**P633** <CorpActnEvtPrcgStsAdvc>

**P634** 	<NtfctnId>

**P635** 		<Id>LOCCUS0000000001</Id>

**P636** 	</NtfctnId>

**P637** 	<OthrDocId>

**P638** 		<Id>

**P639** 			<AcctSvcrDocId>253147815</AcctSvcrDocId>

**P640** 		</Id>

**P641** 		<DocNb>

**P642** 			<LngNb>seev.035.001.16</LngNb>

**P643** 		</DocNb>

**P644** 	</OthrDocId>

**P645** 	<CorpActnGnlInf>

**P646** 		<CorpActnEvtId>DIVGLAX123</CorpActnEvtId>

**P647** 		<OffclCorpActnEvtId>BI01593212345</OffclCorpActnEvtId>

**P648** 		<EvtTp>

**P649** 			<Cd>DVOP</Cd>

**P650** 		</EvtTp>

**P651** 	</CorpActnGnlInf>

**P652** 	<EvtPrcgSts>

**P653** 		<Pdg>

**P654** 			<Rsn>

**P655** 				<RsnCd>

**P656** 					<Cd>NSEC</Cd>

**P657** 				</RsnCd>

**P658** 			</Rsn>

**P659** 		</Pdg>

**P660** 	</EvtPrcgSts>

**P661** </CorpActnEvtPrcgStsAdvc>

**P662** </Document>

**P663**   


