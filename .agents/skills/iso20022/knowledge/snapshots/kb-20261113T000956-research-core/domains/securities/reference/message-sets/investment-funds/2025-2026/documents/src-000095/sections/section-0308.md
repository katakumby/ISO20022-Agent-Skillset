---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Transfer - Matched Leg Transfer (MLT)", "TransferOutInstruction sese.001.001.10"]
content_origin: "source-transcription"
---

# TransferOutInstruction sese.001.001.10

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Transfer - Matched Leg Transfer (MLT) / TransferOutInstruction sese.001.001.10.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P4851** TransferOutInstruction sese.001.001.10

**P4852** Description

**P4853** A TransferOutInstruction message is sent by the instructing party (old plan manager/transferor) to the executing party. In this scenario, the executing party is the transfer agent FUNBGB22. The TransferOutInstruction message is an instruction to transfer 300 units of the fund ISIN GB4444444444, Ethical Blue Fund, from the account of BDAPGB22 (transferor), account 888888 to the account of PEFIGB22 (transferee), account 55555, at FUNBGB22. 

**P4854** The sender, the transferor (the old plan manager) assigns the reference BDAP-TO-002 to the transfer out instruction.

**P4855** The transfer process is a matched/double leg transfer (MLT), the BusinessFlowType element contains DLPR (double leg process).

**P4856** Message Instance

**P4857** <TrfOutInstr>

**P4858** 		<MsgId>

**P4859** 			<Id>IP1-0020</Id>

**P4860** 			<CreDtTm>2026-03-07T10:15:00</CreDtTm>

**P4861** 		</MsgId>

**P4862** 		<TrfDtls>

**P4863** 			<TrfRef>BDAP-TO-002</TrfRef>

**P4864** 			<BizFlowTp>DLPR</BizFlowTp>

**P4865** 			<FinInstrmDtls>

**P4866** 				<Id>

**P4867** 					<ISIN>GB4444444444</ISIN>

**P4868** 				</Id>

**P4869** 				<Nm>Ethical Blue Fund </Nm>

**P4870** 			</FinInstrmDtls>

**P4871** 			<Qty>

**P4872** 				<TtlUnitsNb>300</TtlUnitsNb>

**P4873** 			</Qty>

**P4874** 		</TrfDtls>

**P4875** 		<AcctDtls>

**P4876** 			<AcctId>888888</AcctId>

**P4877** 		</AcctDtls>

**P4878** 		<SttlmDtls>

**P4879** 			<Trfee>

**P4880** 				<Pty>

**P4881** 				<AnyBIC>PEFIGB22</AnyBIC>

**P4882** 				</Pty>

**P4883** 			</Trfee>

**P4884** 			<TrfeeRegdAcct>

**P4885** 				<Id>555555</Id>

**P4886** 				<Svcr>

**P4887** 					<Pty>

**P4888** 						<AnyBIC>FUNBGB22</AnyBIC>

**P4889** 					</Pty>

**P4890** 				</Svcr>

**P4891** 			</TrfeeRegdAcct>

**P4892** 		</SttlmDtls>

**P4893** </TrfOutInstr>

