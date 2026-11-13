---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Order and Confirmation", "Redemption", "RedemptionBulkOrder setr.001.001.05"]
content_origin: "source-transcription"
---

# RedemptionBulkOrder setr.001.001.05

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Order and Confirmation / Redemption / RedemptionBulkOrder setr.001.001.05.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P2697** RedemptionBulkOrder setr.001.001.05

**P2698** Description

**P2699** A RedemptionBulkOrder message is sent for financial instrument ISIN FR1234567890. It contains two orders.

**P2700** The first individual order has order reference 1111 and is for account 001-56576576. For this account, 100 units are to be redeemed. There will be no physical delivery.

**P2701** The second individual order has order reference 2222 and is for account 007-23415354. For this account, 50 units are to be redeemed. There will be no physical delivery. The requested settlement currency for all the orders in the message is EUR.

**P2702** Message Instance

**P2703** <RedBlkOrdr>

**P2704** 	<MsgId>

**P2705** 		<Id>R0001</Id>

**P2706** 		<CreDtTm>2026-01-04T09:30:30</CreDtTm>

**P2707** 	</MsgId>

**P2708** 	<BlkOrdrDtls>

**P2709** 		<FinInstrmDtls>

**P2710** 			<Id>

**P2711** 				<ISIN>FR1234567890</ISIN>

**P2712** 			</Id>

**P2713** 		</FinInstrmDtls>

**P2714** 		<IndvOrdrDtls>

**P2715** 			<OrdrRef>1111</OrdrRef>

**P2716** 			<InvstmtAcctDtls>

**P2717** 				<AcctId>001-56576576</AcctId>

**P2718** 			</InvstmtAcctDtls>

**P2719** 			<AmtOrUnitsOrPctg>

**P2720** 				<UnitsNb>100</UnitsNb>

**P2721** 			</AmtOrUnitsOrPctg>

**P2722** 			<PhysDlvryInd>false</PhysDlvryInd>

**P2723** 		</IndvOrdrDtls>

**P2724** 		<IndvOrdrDtls>

**P2725** 			<OrdrRef>2222</OrdrRef>

**P2726** 			<InvstmtAcctDtls>

**P2727** 				<AcctId>007-23415354</AcctId>

**P2728** 			</InvstmtAcctDtls>

**P2729** 			<AmtOrUnitsOrPctg>

**P2730** 				<UnitsNb>50</UnitsNb>

**P2731** 			</AmtOrUnitsOrPctg>

**P2732** 			<PhysDlvryInd>false</PhysDlvryInd>

**P2733** 		</IndvOrdrDtls>

**P2734** 		<ReqdSttlmCcy>EUR</ReqdSttlmCcy>

**P2735** 	</BlkOrdrDtls>

**P2736** </RedBlkOrdr>

