---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "FinancialInstitutionCreditTransfer pacs.009.001.13 - 1", "Second FinancialInstitutionCreditTransfer"]
content_origin: "source-transcription"
---

# Second FinancialInstitutionCreditTransfer

Source: [src-000162](../../../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Locator: heading path Business Examples / FinancialInstitutionCreditTransfer pacs.009.001.13 - 1 / Second FinancialInstitutionCreditTransfer.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P2148** Second FinancialInstitutionCreditTransfer

**P2149** Description 

**P2150** On receipt of the instruction of BBBB Bank, CCCC Bank forwards the FinancialInstitutionCreditTransfer to the creditor agent AAAAJPJT. CCCC Bank holds multiple accounts with AAAAJPJT, and specifies that account 3451571 has to be used for reimbursement.

**P2151** Business Data

**P2152** FinancialInstitutionCreditTransfer from CCCCJPJT to AAAAJPJT:

[T42 - complete table](../tables/tbl-0042.md)

**P2153** Message Instance

**P2154** <FICdtTrf>

**P2155** 	<GrpHdr>

**P2156** 		<MsgId>CCCC/150929-FICT/743</MsgId>

**P2157** 		<CreDtTm>2015-09-29T08:00:10</CreDtTm>

**P2158** 		<NbOfTxs>1</NbOfTxs>

**P2159** 		<SttlmInf>

**P2160** 			<SttlmMtd>INDA</SttlmMtd>

**P2161** 			<SttlmAcct>

**P2162** 				<Id>

**P2163** 					<Othr>

**P2164** 						<Id>3451571</Id>

**P2165** 					</Othr>

**P2166** 				</Id>

**P2167** 			</SttlmAcct>

**P2168** 		</SttlmInf>

**P2169** 	<InstgAgt>

**P2170** 			<FinInstnId>

**P2171** 				<BICFI>CCCCJPJT</BICFI>

**P2172** 			</FinInstnId>

**P2173** 		</InstgAgt>

**P2174** 		<InstdAgt>

**P2175** 			<FinInstnId>

**P2176** 				<BICFI>AAAAJPJT</BICFI>

**P2177** 			</FinInstnId>

**P2178** 		</InstdAgt>

**P2179** 	</GrpHdr>

**P2180** 	<CdtTrfTxInf>

**P2181** 		<PmtId>

**P2182** 			<InstrId>CCCC/150929-FICT/743/1</InstrId>

**P2183** 			<EndToEndId>ABC/4562/2015-09-08</EndToEndId>

**P2184** 			<TxId>BBBB/150928-CCT/JPY/123/1</TxId>

**P2185** 		</PmtId>

**P2186** 		<IntrBkSttlmAmt Ccy="JPY">10000000</IntrBkSttlmAmt>

**P2187** 		<IntrBkSttlmDt>2015-09-29</IntrBkSttlmDt>

**P2188** 		<Dbtr>

**P2189** 			<FinInstnId>

**P2190** 				<BICFI>BBBBUS33</BICFI>

**P2191** 			</FinInstnId>

**P2192** 		</Dbtr>

**P2193** 		<Cdtr>

**P2194** 			<FinInstnId>

**P2195** 				<BICFI>AAAAGB2L</BICFI>

**P2196** 			</FinInstnId>

**P2197** 		</Cdtr>

**P2198** 	</CdtTrfTxInf>

**P2199** </FICdtTrf>

