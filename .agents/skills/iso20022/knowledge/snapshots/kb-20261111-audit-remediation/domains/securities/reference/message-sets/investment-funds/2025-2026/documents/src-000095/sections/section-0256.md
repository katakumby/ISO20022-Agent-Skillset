---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Order Status", "OrderInstructionStatusReport setr.016.001.05 – 2 Accepted"]
content_origin: "source-transcription"
---

# OrderInstructionStatusReport setr.016.001.05 – 2 Accepted

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Order Status / OrderInstructionStatusReport setr.016.001.05 – 2 Accepted.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P3758** OrderInstructionStatusReport setr.016.001.05 – 2 Accepted

**P3759** Description

**P3760** An OrderInstructionStatusReport message is sent to report on the status of an order. It reports that an order with order reference REF A has been accepted. 

**P3761** The message also pre-confirms that the expected cash settlement date of the order is 10 January 2026.

**P3762** Message Instance

**P3763** <OrdrInstrStsRpt>

**P3764** 	<MsgId>

**P3765** 		<Id>O0001</Id>

**P3766** 		<CreDtTm>2026-01-08T09:30:30</CreDtTm>

**P3767** 	</MsgId>

**P3768** 	<StsRpt>

**P3769** 		<IndvOrdrDtlsRpt>

**P3770** 			<OrdrRef>REF A</OrdrRef>

**P3771** 			<OrdrSts>

**P3772** 			<Sts>PACK</Sts>

**P3773** 			</OrdrSts>

**P3774** 			<NewDtls>

**P3775** 				<XpctdCshSttlmDt>2026-01-10</XpctdCshSttlmDt>

**P3776** 			</NewDtls>

**P3777** 		</IndvOrdrDtlsRpt>

**P3778** 	</StsRpt>

**P3779** </OrdrInstrStsRpt>

