---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["Examples", "Intra-balance Movement Modification Request - camt.072.001"]
content_origin: "source-transcription"
---

# Intra-balance Movement Modification Request - camt.072.001

Source: [src-000359](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Locator: heading path Examples / Intra-balance Movement Modification Request - camt.072.001.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P510** Intra-balance Movement Modification Request - camt.072.001

**P511** Description

**P512** In this example Party A (PRTYABICXXX) has requested the amendment of the priority to ‘High’, on an existing cash Settlement Restriction with an account owner transaction id, ‘REF0123’. The original cash Settlement Restriction requested the ‘Normal’ priority blocking of 50000 EUR for the sub balance ‘BLKA’, of the cash account, ‘1000000123’, settling on the 9th of January 2015.

**P513** Message instance

**P514** <Document>

**P515** 	<IntraBalMvmntModReq>

**P516** 	       <Id>

**P517** 		       <Id>DOC1234</Id>

**P518** 	       </Id>

**P519** 		<CshAcct>

**P520** 		       <Id>

**P521** 			       <Othr>

**P522** 				       <Id>1000000123</Id>

**P523** 			       </Othr>

**P524** 		       </Id>

**P525** 		</CshAcct>

**P526** 		<CshAcctOwnr>

**P527** 			<Id>

**P528** 				<Id>

**P529** 					<AnyBIC>PRTYABICXXX</AnyBIC>

**P530** 				</Id>

**P531** 			</Id>

**P532** 		</CshAcctOwnr>

**P533** 		<ReqDtls>

**P534** 			<Ref>

**P535** 			       <AcctOwnrTxId>REF0123</AcctOwnrTxId>

**P536** 			</Ref>

**P537** 			<Prty>

**P538** 				<Nmrc>0003</Nmrc>

**P539** 			</Prty>

**P540** 		</ReqDtls>

**P541** 		<UndrlygIntraBal>

**P542** 			<SttlmAmt>

**P543** 				<AmtWthCcy Ccy="EUR">50000</AmtWthCcy>

**P544** 			</SttlmAmt>

**P545** 			<SttlmDt>

**P546** 				<Dt>2015-01-09</Dt>

**P547** 			</SttlmDt>

**P548** 			<BalFr>

**P549** 				<Tp>

**P550** 					<Prtry>

**P551** 						<Id>DLVR</Id>

**P552** 						<Issr>T2S</Issr>

**P553** 						<SchmeNm>RT</SchmeNm>

**P554** 					</Prtry>

**P555** 				</Tp>

**P556** 			</BalFr>

**P557** 			<BalTo>

**P558** 				<Tp>

**P559** 					<Prtry>

**P560** 						<Id>BLKA</Id>

**P561** 						<Issr>T2S</Issr>

**P562** 						<SchmeNm>RT</SchmeNm>

**P563** 					</Prtry>

**P564** 				</Tp>

**P565** 			</BalTo>

**P566** 			<Prty>

**P567** 				<Nmrc>0004</Nmrc>

**P568** 			</Prty>

**P569** 		</UndrlygIntraBal>

**P570** 	</IntraBalMvmntModReq>

**P571** </Document>

