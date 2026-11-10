---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["Business Examples", "CorporateActionInstruction seev.033.00x.14"]
content_origin: "source-transcription"
---

# CorporateActionInstruction seev.033.00x.14

Source: [src-000079](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Locator: heading path Business Examples / CorporateActionInstruction seev.033.00x.14.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P664** CorporateActionInstruction seev.033.00x.14

**P665** Description

**P666** This example describes a CorporateActionInstruction sent by an account owner. The client elects the securities option for the entire eligible balance.

**P667** The CorporateActionInstruction sample message illustrates an instruction based on the event announced in the example 1 of the CorporateActionNotification section.

**P668** The corporate action event is a distribution of a dividend to shareholders with a choice of benefit to receive. Shareholders may choose to receive shares, cash.

**P669** Business Data

**P670** Issue name

**P671** Glaxo Holdings

**P672** ISIN GB0007123466

**P673** Terms

**P674** Final dividend of GBP 0,017 per share, OR one ordinary share for every 37 shares held. Elections cannot be made on holdings of less than 37 shares.

**P675** Elections which give rise to fractional entitlements will be rounded down to the nearest whole multiple of 37 shares; the full cash dividend of GBP 0,017 per share will be paid on the remainder of the holding.

**P676** Relative dates

**P677** Ex date - 01 September 2010

**P678** Record date - 07 September 2010

**P679** Dividend payment date - 02 October 2010

**P680** Response deadline date - 23 September 2010

**P681** Transaction description

**P682** A/C 98-0112441-05 has an underlying balance of 80.000 shares.

**P683** Message Instance (with application header)

**P684** <AppHdr xmlns="urn:iso:std:iso:20022:tech:xsd:head.001.001.02" xmlns:n1="http://www.w3.org/2000/09/xmldsig#">

**P685** 	<Fr>

**P686** 		<FIId>

**P687** 			<FinInstnId>

**P688** 				<BICFI>WXYZFRPP666</BICFI>

**P689** 			</FinInstnId>

**P690** 		</FIId>

**P691** 	</Fr>

**P692** 	<To>

**P693** 		<FIId>

**P694** 			<FinInstnId>

**P695** 				<BICFI>ABCDBEBBXXX</BICFI>

**P696** 			</FinInstnId>

**P697** 		</FIId>

**P698** 	</To>

**P699** 	<BizMsgIdr>GLOCUS0000000001</BizMsgIdr>

**P700** 	<MsgDefIdr>seev.033.001.14</MsgDefIdr>

**P701** 	<CreDt>2010-10-03T09:30:00Z</CreDt>

**P702** </AppHdr>

**P703** <Document xmlns="urn:iso:std:iso:20022:tech:xsd:seev.033.001.14" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

**P704** 	<CorpActnInstr>

**P705** 		<OthrDocId>

**P706** 			<Id>

**P707** 				<AcctSvcrDocId>LOCCUS000000001</AcctSvcrDocId>

**P708** 			</Id>

**P709** 			<DocNb>

**P710** 				<LngNb>seev.031.001.15</LngNb>

**P711** 			</DocNb>

**P712** 		</OthrDocId>

**P713** 		<CorpActnGnlInf>

**P714** 			<CorpActnEvtId>DIVGLAX123</CorpActnEvtId>

**P715** 			<OffclCorpActnEvtId>BI01593212345</OffclCorpActnEvtId>

**P716** 			<EvtTp>

**P717** 				<Cd>DVOP</Cd>

**P718** 			</EvtTp>

**P719** 			<UndrlygScty>

**P720** 				<FinInstrmId>

**P721** 					<ISIN>GB0007123466</ISIN>

**P722** 					<Desc>GLAXO HOLDINGS</Desc>

**P723** 				</FinInstrmId>

**P724** 			</UndrlygScty>

**P725** 		</CorpActnGnlInf>

**P726** 		<AcctDtls>

**P727** 			<SfkpgAcct>98-0112441-05</SfkpgAcct>

**P728** 			<Bal>

**P729** 				<TtlElgblBal>

**P730** 					<QtyChc>

**P731** 						<SgndQty>

**P732** 							<ShrtLngPos>LONG</ShrtLngPos>

**P733** 							<Qty>

**P734** 								<Unit>80000</Unit>

**P735** 							</Qty>

**P736** 						</SgndQty>

**P737** 					</QtyChc>

**P738** 				</TtlElgblBal>

**P739** 			</Bal>

**P740** 		</AcctDtls>

**P741** 		<CorpActnInstr>

**P742** 			<OptnNb>

**P743** 				<Nb>002</Nb>

**P744** 			</OptnNb>

**P745** 			<OptnTp>

**P746** 				<Cd>SECU</Cd>

**P747** 			</OptnTp>

**P748** 				<SctiesQtyOrInstdAmt>

**P749** 					<SctiesQty>

**P750** 						<InstdQty>

**P751** 							<Qty>

**P752** 								<Unit>80000</Unit>

**P753** 							</Qty>

**P754** 						</InstdQty>

**P755** 					</SctiesQty>

**P756** 			</SctiesQtyOrInstdAmt>

**P757** 		</CorpActnInstr>

**P758** 	</CorpActnInstr>

**P759** </Document>  


