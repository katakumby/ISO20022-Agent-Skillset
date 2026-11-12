---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000004"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "BankToCustomerDebitCreditNotification camt.054.001.14"]
content_origin: "source-transcription"
---

# BankToCustomerDebitCreditNotification camt.054.001.14

Source: [src-000004](../../../../../../../../../evidence/omitted/52f543e2b58f688bc16fa140.md). Locator: heading path Business Examples / BankToCustomerDebitCreditNotification camt.054.001.14.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P443** BankToCustomerDebitCreditNotification camt.054.001.14

**P444** Description

**P445** Besides providing an intraday account report at 12.30 PM (see example with BankToCustomerAccountReport), AAAA Banken and Finpetrol have agreed on a credit notification service, for all incoming credits above a certain threshold. On 18 October 2010, at 1.20 PM, AAAASESS sends a BankToCustomerDebitCreditNotification to Company Finpetrol, to advise Finpetrol of an incoming credit on its account.

**P446** Business Data

[T20 - complete table](../tables/tbl-0020.md)

**P447** Message Instance

**P448** <BkToCstmrDbtCdtNtfctn>

**P449** 	<GrpHdr>

**P450** 		<MsgId>AAAASESS-FP-00001</MsgId>

**P451** 		<CreDtTm>2015-10-18T13:20:00+01:00</CreDtTm>

**P452** 	</GrpHdr>

**P453** 	<Ntfctn>

**P454** 		<Id>AAAASESS-FP-CN-98765</Id>

**P455** 		<CreDtTm>2015-10-18T13:20:00+01:00</CreDtTm>

**P456** 		<Acct>

**P457** 			<Id>

**P458** 				<Othr>

**P459** 					<Id>50000000054910000003</Id>

**P460** 				</Othr>

**P461** 			</Id>

**P462** 			<Ownr>

**P463** 				<Nm>FINPETROL</Nm>

**P464** 			</Ownr>

**P465** 			<Svcr>

**P466** 				<FinInstnId>

**P467** 					<Nm>AAAA BANKEN</Nm>

**P468** 					<PstlAdr>

**P469** 						<Ctry>SE</Ctry>

**P470** 					</PstlAdr>

**P471** 				</FinInstnId>

**P472** 			</Svcr>

**P473** 		</Acct>

**P474** 		<Ntry>

**P475** 			<Amt Ccy="SEK">105678.50</Amt>

**P476** 			<CdtDbtInd>CRDT</CdtDbtInd>

**P477** 			<Sts>

**P478** 				<Cd>BOOK</Cd>

**P479** 			</Sts>

**P480** 			<BookgDt>

**P481** 				<DtTm>2015-10-18T13:15:00+01:00</DtTm>

**P482** 			</BookgDt>

**P483** 			<ValDt>

**P484** 				<Dt>2015-10-18</Dt>

**P485** 			</ValDt>

**P486** 			<AcctSvcrRef>AAAASESS-FP-CN-98765/01</AcctSvcrRef>

**P487** 			<BkTxCd>

**P488** 				<Domn>

**P489** 					<Cd>PAYM</Cd>

**P490** 					<Fmly>

**P491** 						<Cd>0001</Cd>

**P492** 						<SubFmlyCd>0005</SubFmlyCd>

**P493** 					</Fmly>

**P494** 				</Domn>

**P495** 			</BkTxCd>

**P496** 			<NtryDtls>

**P497** 				<TxDtls>

**P498** 					<Refs>

**P499** 						<EndToEndId>MUELL/FINP/RA12345</EndToEndId>

**P500** 					</Refs>

**P501** 					<Amt Ccy="SEK">0</Amt>

**P502** 					<CdtDbtInd>CRDT</CdtDbtInd>

**P503** 					<RltdPties>

**P504** 						<Dbtr>

**P505** 							<Pty>

**P506** 								<Nm>MUELLER</Nm>

**P507** 							</Pty>

**P508** 						</Dbtr>

**P509** 					</RltdPties>

**P510** 				</TxDtls>

**P511** 			</NtryDtls>

**P512** 		</Ntry>

**P513** 	</Ntfctn>

**P514** </BkToCstmrDbtCdtNtfctn>

