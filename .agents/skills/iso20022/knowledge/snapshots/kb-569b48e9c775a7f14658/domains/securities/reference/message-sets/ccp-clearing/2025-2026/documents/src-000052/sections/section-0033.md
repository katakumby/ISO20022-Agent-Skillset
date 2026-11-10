---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Margining BusinessTransaction"]
content_origin: "source-transcription"
---

# Margining BusinessTransaction

Source: [src-000052](../../../../../../../../../evidence/omitted/b45c53bac2be08dee677b607.md). Locator: heading path BusinessTransactions / Margining BusinessTransaction.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P229** Margining BusinessTransaction

**P230** The central counterparty (CCP) calculates the risk linked to the net position of each clearing member. The MarginReport message is sent by a CCP to the clearing member to report on:

**P231** the exposure resulting from the trade positions

**P232** the value of the collateral held by the CCP (market value of this collateral)

**P233** the resulting difference representing the risk encountered by the CCP.

**P234** Optional flows:

**P235** Depending on the CCP’s internal rules:

**P236** The CCP may send the MarginCallRequest message in case the risk that has been calculated is greater than the amount of collateral that has been posted by the clearing member.

**P237** The clearing member may propose specific collateral to cover the risk encountered by the CCP. In this case, the clearing member sends the CollateralProposal message. The CCP may respond using the CollateralProposalResponse message to either accept or reject the piece of collateral that was proposed by the clearing member. (This sequence of messages can be repeated in case of rejection of the collateral proposed).

**P238** Note that these optional flows are not part of the scope of this project and will not be described in this document. They are only shown for the sake of completeness. For more information please refer to the Collateral Management project.

[fig-0015 - original figure evidence](../diagrams/fig-0015.md)

