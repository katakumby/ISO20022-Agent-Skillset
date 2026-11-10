---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Portfolio Transfer", "PortfolioTransferCancellationRequest sese.014.001.09"]
content_origin: "source-transcription"
---

# PortfolioTransferCancellationRequest sese.014.001.09

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Portfolio Transfer / PortfolioTransferCancellationRequest sese.014.001.09.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P4614** PortfolioTransferCancellationRequest sese.014.001.09

**P4615** Description	

**P4616** A PortfolioTransferCancellationRequest message is sent by the new plan manager (transferee/acquiring party), PEFIGB2, to the old plan manager (transferor/ceding party), BDAPGB22, to request the cancellation of a previously sent PortfolioTransferInstruction (sese.012) message.

**P4617** The reference assigned in the original PortfolioTransferInstruction (sese.012) message for the portfolio transfer is PORT-GB-001 and this reference is specified in the PortfolioTransferCancellationRequest message in the TransferReference element.

**P4618** Message Instance

**P4619** <PrtflTrfCxlReq>

**P4620** 		<MsgRef>

**P4621** 			<Id>IP-0003</Id>

**P4622** 			<CreDtTm>2019-03-05T10:50:00</CreDtTm>

**P4623** 		</MsgRef>

**P4624** 		<TrfRefs>

**P4625** 			<TrfRef>PORT-GB-001</TrfRef>

**P4626** 		</TrfRefs>

**P4627** </PrtflTrfCxlReq>

