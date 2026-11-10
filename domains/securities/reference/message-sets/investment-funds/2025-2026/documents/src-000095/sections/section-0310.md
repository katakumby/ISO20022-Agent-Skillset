---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Transfer - Matched Leg Transfer (MLT)", "TransferInInstruction sese.005.001.10"]
content_origin: "source-transcription"
---

# TransferInInstruction sese.005.001.10

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Transfer - Matched Leg Transfer (MLT) / TransferInInstruction sese.005.001.10.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P4939** TransferInInstruction sese.005.001.10

**P4940** Description

**P4941** A TransferInInstruction message is sent by the instructing party (new plan manager/transferor) to the executing party. In this scenario, the executing party is the transfer agent FUNBGB22. The TransferInInstruction message is an instruction to transfer 300 units of the fund ISIN GB4444444444, Ethical Blue Fund, into the account of PEFIGB22 (transferee), account 555555, at FUNBGB22 from the account of BDAPGB22 (transferor), account 888888, at FUNBGB22. 

**P4942** The sender, the transferee (the new plan manager) assigns the reference, PEFI-TI-002 to the transfer in instruction.

**P4943** The transfer process is a matched/double leg transfer (MLT), the BusinessFlowType element contains DLPR (double leg process).

**P4944** Message Instance

**P4945** <TrfInInstr>

**P4946** 		<MsgId>

**P4947** 			<Id>IP2-0029</Id>

**P4948** 			<CreDtTm>2026-03-07T10:25:00</CreDtTm>

**P4949** 		</MsgId>

**P4950** 		<TrfDtls>

**P4951** 			<TrfRef>PEFI-TI-002 </TrfRef>

**P4952** 			<BizFlowTp>DLPR</BizFlowTp>

**P4953** 			<FinInstrmDtls>

**P4954** 				<Id>

**P4955** 					<ISIN>GB4444444444</ISIN>

**P4956** 				</Id>

**P4957** 				<Nm>Ethical Blue Fund </Nm>

**P4958** 			</FinInstrmDtls>

**P4959** 			<Qty>

**P4960** 				<TtlUnitsNb>300</TtlUnitsNb>

**P4961** 			</Qty>

**P4962** 		</TrfDtls>

**P4963** 		<AcctDtls>

**P4964** 			<AcctId>555555</AcctId>

**P4965** 		</AcctDtls>

**P4966** 		<SttlmDtls>

**P4967** 			<Trfr>

**P4968** 				<Pty>

**P4969** 					<AnyBIC>BDAPGB22</AnyBIC>

**P4970** 				</Pty>

**P4971** 			</Trfr>

**P4972** 			<TrfrRegdAcct>

**P4973** 				<Id>88888888</Id>

**P4974** 				<Svcr>

**P4975** 					<Pty>

**P4976** 						<AnyBIC>FUNBGB22</AnyBIC>

**P4977** 					</Pty>

**P4978** 				</Svcr>

**P4979** 			</TrfrRegdAcct>

**P4980** 		</SttlmDtls>

**P4981** 	</TrfInInstr>

