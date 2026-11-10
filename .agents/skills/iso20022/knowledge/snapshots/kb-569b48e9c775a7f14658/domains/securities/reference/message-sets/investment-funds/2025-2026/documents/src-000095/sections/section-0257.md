---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Order Status", "OrderInstructionStatusReport setr.016.001.05 – 3 Suspended "]
content_origin: "source-transcription"
---

# OrderInstructionStatusReport setr.016.001.05 – 3 Suspended 

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Order Status / OrderInstructionStatusReport setr.016.001.05 – 3 Suspended .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P3780** OrderInstructionStatusReport setr.016.001.05 – 3 Suspended 

**P3781** Description

**P3782** An OrderInstructionStatusReport message is sent to report on the status of an order. It reports that an order with order reference Order 14 is suspended because the fund management company, FUNALULL, has indicated that the pricing is suspended. The fund management company is reported as the status initiator.

**P3783** Message Instance

**P3784** <OrdrInstrStsRpt>

**P3785** 	<MsgId>

**P3786** 		<Id>O0001</Id>

**P3787** 		<CreDtTm>2026-01-08T09:30:30</CreDtTm>

**P3788** 	</MsgId>

**P3789** 	<StsRpt>

**P3790** 		<IndvOrdrDtlsRpt>

**P3791** 			<OrdrRef>Order 14</OrdrRef>

**P3792** 			<OrdrSts>

**P3793** 				<Sspd>

**P3794** 					<RsnDtls>

**P3795** 						<Rsn>

**P3796** 							<Cd>PRIC</Cd>

**P3797** 						</Rsn>

**P3798** 					</RsnDtls>

**P3799** 				</Sspd>

**P3800** 			</OrdrSts>

**P3801** 			<StsInitr>

**P3802** 				<Pty>

**P3803** 					<AnyBIC>FUNALULL</AnyBIC>

**P3804** 				</Pty>

**P3805** 			</StsInitr>

**P3806** 		</IndvOrdrDtlsRpt>

**P3807** 	</StsRpt>

**P3808** </OrdrInstrStsRpt>

