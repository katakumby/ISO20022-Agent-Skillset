---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["Business Examples", "CorporateActionInstructionStatusAdvice seev.034.00x.16"]
content_origin: "source-transcription"
---

# CorporateActionInstructionStatusAdvice seev.034.00x.16

Source: [src-000079](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Locator: heading path Business Examples / CorporateActionInstructionStatusAdvice seev.034.00x.16.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P760** CorporateActionInstructionStatusAdvice seev.034.00x.16

**P761** Description

**P762** This example describes a CorporateActionInstructionStatusAdvice sent by an account servicer to the account owner. The status advice informs the account owner that its instruction to elect the securities option for its entire eligible balance has been accepted for further processing.

**P763** This CorporateActionInstructionStatusAdvice sample message illustrates the status of the instruction message illustrated in the example 1 of the CorporateActionInstruction section.

**P764** The corporate action event is a distribution of a dividend to shareholders with a choice of benefit to receive. Shareholders may choose to receive shares, cash.

**P765** Business Data

**P766** Issue name

**P767** Glaxo Holdings

**P768** ISIN GB0007123466

**P769** Terms

**P770** Final dividend of GBP 0,017 per share, OR one ordinary share for every 37 shares held. Elections cannot be made on holdings of less than 37 shares.

**P771** Elections which give rise to fractional entitlements will be rounded down to the nearest whole multiple of 37 shares; the full cash dividend of GBP 0,017 per share will be paid on the remainder of the holding.

**P772** Relative dates

**P773** Ex date - 01 September 2010

**P774** Record date - 07 September 2010

**P775** Dividend payment date - 02 October 2010

**P776** Response deadline date - 23 September 2010

**P777** Transaction description

**P778** A/C 98-0112441-05 has an underlying balance of 80,000 shares.

**P779** Message Instance (with application header)

**P780** <AppHdr xmlns="urn:iso:std:iso:20022:tech:xsd:head.001.001.02" xmlns:n1="http://www.w3.org/2000/09/xmldsig#">

**P781** 	<Fr>

**P782** 		<FIId>

**P783** 			<FinInstnId>

**P784** 				<BICFI>ABCDBEBBXXX</BICFI>

**P785** 			</FinInstnId>

**P786** 		</FIId>

**P787** 	</Fr>

**P788** 	<To>

**P789** 		<FIId>

**P790** 			<FinInstnId>

**P791** 				<BICFI>WXYZFRPP666</BICFI>

**P792** 			</FinInstnId>

**P793** 		</FIId>

**P794** 	</To>

**P795** 	<BizMsgIdr>LOCCUS0000000055</BizMsgIdr>

**P796** 	<MsgDefIdr>seev.034.001.16</MsgDefIdr>

**P797** 	<CreDt>2010-09-09T09:30:00Z</CreDt>

**P798** </AppHdr>

**P799** <Document xmlns="urn:iso:std:iso:20022:tech:xsd:seev.034.001.16" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

**P800** <CorpActnInstrStsAdvc>

**P801** 	<InstrId>

**P802** 		<Id>GLOCUS0000000001</Id>

**P803** 	</InstrId>

**P804** 	<CorpActnGnlInf>

**P805** 		<CorpActnEvtId>DIVGLAX123</CorpActnEvtId>

**P806** 		<OffclCorpActnEvtId>BI01593212345</OffclCorpActnEvtId>

**P807** 		<EvtTp>

**P808** 			<Cd>DVOP</Cd>

**P809** 		</EvtTp>

**P810** 	</CorpActnGnlInf>

**P811** <InstrPrcgSts>

**P812** <AccptdForFrthrPrcg>

**P813** <AccptdRsn>

**P814** <NoSpcfdRsn>NORE</NoSpcfdRsn>

**P815** </AccptdRsn>

**P816** </AccptdForFrthrPrcg>	

**P817** 	</InstrPrcgSts>

**P818** 	<CorpActnInstr>

**P819** 		<OptnNb>

**P820** 			<Nb>002</Nb>

**P821** 		</OptnNb>

**P822** 		<OptnTp>

**P823** 			<Cd>SECU</Cd>

**P824** 		</OptnTp>

**P825** 		<StsQty>

**P826** 			<Qty>

**P827** 				<Unit>80000</Unit>

**P828** 			</Qty>

**P829** 		</StsQty>

**P830** 	</CorpActnInstr>

**P831** </CorpActnInstrStsAdvc>

**P832** </Document>

**P833**   


