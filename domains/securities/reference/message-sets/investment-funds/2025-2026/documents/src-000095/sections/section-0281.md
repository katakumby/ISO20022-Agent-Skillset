---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Portfolio Transfer", "TransferInstructionStatusReport sese.011.001.10 – Payment Advice"]
content_origin: "source-transcription"
---

# TransferInstructionStatusReport sese.011.001.10 – Payment Advice

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Portfolio Transfer / TransferInstructionStatusReport sese.011.001.10 – Payment Advice.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P4575** TransferInstructionStatusReport sese.011.001.10 – Payment Advice

**P4576** As a result of a portfolio transfer, two assets are to be transferred as cash for a total value of GBP 11,000.

**P4577** A TransferInstructionStatusReport message, with event type PAYA, is sent to advise the new plan manager (transferee), PEFIGB22, that this cash will be transferred into its account, IBAN GB85324906366027 at BARCGB22 (sort code SC600501) with payment reference PORT-GB-001-PAYM, on 13 March 2026. The cash transfer is in reference to portfolio transfer reference PORT-GB-001 and this reference is specified in the TransferReference element. The status of the portfolio transfer is 'pending settlement' and no reason (NORE) is stated for the status.

**P4578** Message Instance

**P4579** <TrfInstrStsRpt>

**P4580** 		<MsgId>

**P4581** 			<Id>EP-0003</Id>

**P4582** 			<CreDtTm>2026-03-11T10:25:00</CreDtTm>

**P4583** 		</MsgId>

**P4584** 		<StsRpt>

**P4585** 			<TrfRef>PORT-GB-001</TrfRef>

**P4586** 			<TrfEvtTp>

**P4587** 				<Cd>PAYA</Cd>

**P4588** 			</TrfEvtTp>

**P4589** 			<TrfSts>

**P4590** 				<PdgSttlm>

**P4591** 					<NoSpcfdRsn>NORE</NoSpcfdRsn>

**P4592** 				</PdgSttlm>

**P4593** 			</TrfSts>

**P4594** 			<PmtDtls>

**P4595** 				<Ref> PORT-GB-001-PAYM </Ref>

**P4596** 				<Amt Ccy="GBP">11000</Amt>

**P4597** 				<PmtDt>2026-03-13</PmtDt>

**P4598** 				<CshSttlmDtls>

**P4599** 				<CdtTrfDtls>

**P4600** 						<CdtrAgt>

**P4601** 							<BICFI>BARCGB22</BICFI>

**P4602** 							<ClrSysMmbId>

**P4603** 								<GBSC>SC600501</GBSC>

**P4604** 							</ClrSysMmbId>

**P4605** 						</CdtrAgt>

**P4606** 						<CdtrAcct>

**P4607** 							<IBAN>GB85324906366027</IBAN>

**P4608** 						</CdtrAcct>

**P4609** 					</CdtTrfDtls>

**P4610** 				</CshSttlmDtls>

**P4611** 			</PmtDtls>

**P4612** 		</StsRpt>

**P4613** </TrfInstrStsRpt>

