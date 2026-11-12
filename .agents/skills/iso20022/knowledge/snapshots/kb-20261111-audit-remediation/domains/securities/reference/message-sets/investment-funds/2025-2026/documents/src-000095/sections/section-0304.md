---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Transfer - Single Leg Transfer (SLT) ", "TransferOutInstruction sese.001.001.10"]
content_origin: "source-transcription"
---

# TransferOutInstruction sese.001.001.10

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Transfer - Single Leg Transfer (SLT)  / TransferOutInstruction sese.001.001.10.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P4697** TransferOutInstruction sese.001.001.10

**P4698** Description

**P4699** A TransferOutInstruction message is sent by the instructing party (old plan manager/transferor) to the executing party. In this scenario, the executing party is the transfer agent TATAGB22. The TransferOutInstruction message is an instruction to transfer 2,000 units of the fund ISIN GB1111111111, Ethical Green Fund, from the account of BDAPGB22 (transferor), account 999999, to the account of PEFIGB22 (transferee), account 444444, at TATAGB22.

**P4700** The transfer process is single leg transfer (SLT), the BusinessFlowType element contains SLDP (single leg initiated by the delivery side).

**P4701** References: 'transfer-in side'

**P4702** Two references, as communicated previously to the transferor in the PortfolioTransferInstruction (sese.012) message, are specified:

**P4703** the portfolio transfer reference, PORT-GB-001, as assigned by the transferee (new plan manger) to the transfer of the portfolio as a 'whole'.

**P4704** the reference assigned by the transferee (new plan manger) to the transfer of the individual asset, the units of ISIN GB1111111111, Ethical Green fund is PEFI-TI-U001. The issuer of the reference, PEFIGB22, is also specified with this reference. This reference may also be known as the 'transfer-in reference'.

**P4705** (These two references will be echoed back in the TransferOutConfirmation (sese.003) message and passed on in the TransferInConfirmation (sese.007) message sent by the transfer agent to confirm the subsequent transfer of units.)

**P4706** References: 'transfer-out side'

**P4707** The sender, the transferor (the old plan manager) assigns the reference, BDAP-TO-001, to the transfer out instruction.

**P4708** XML Instance 

**P4709** <TrfOutInstr>

**P4710** 		<MsgId>

**P4711** 			<Id>IP-0010</Id>

**P4712** 			<CreDtTm>2026-03-07T10:15:00</CreDtTm>

**P4713** 		</MsgId>

**P4714** 		<MstrRef>PORT-GB-001</MstrRef>

**P4715** 		<TrfDtls>

**P4716** 			<TrfRef>BDAP-TO-001 </TrfRef>

**P4717** 			<CtrPtyRef>

**P4718** 				<Ref>PEFI-TI-U001</Ref>

**P4719** 				<RefIssr>

**P4720** 					<Pty>

**P4721** 						<AnyBIC>PEFIGB22</AnyBIC>

**P4722** 					</Pty>

**P4723** 				</RefIssr>

**P4724** 			</CtrPtyRef>

**P4725** 			<BizFlowTp>SLDP</BizFlowTp>

**P4726** 			<FinInstrmDtls>

**P4727** 				<Id>

**P4728** 					<ISIN>GB1111111111</ISIN>

**P4729** 				</Id>

**P4730** 				<Nm>Ethical Green Fund </Nm>

**P4731** 			</FinInstrmDtls>

**P4732** 			<Qty>

**P4733** 				<TtlUnitsNb>2000</TtlUnitsNb>

**P4734** 			</Qty>

**P4735** 		</TrfDtls>

**P4736** 		<AcctDtls>

**P4737** 			<AcctId>999999</AcctId>

**P4738** 		</AcctDtls>

**P4739** 		<SttlmDtls>

**P4740** 			<Trfee>

**P4741** 				<Pty>

**P4742** 				<AnyBIC>PEFIGB22</AnyBIC>

**P4743** 				</Pty>

**P4744** 			</Trfee>

**P4745** 			<TrfeeRegdAcct>

**P4746** 				<Id>444444</Id>

**P4747** 			</TrfeeRegdAcct>

**P4748** 		</SttlmDtls>

**P4749** </TrfOutInstr>

