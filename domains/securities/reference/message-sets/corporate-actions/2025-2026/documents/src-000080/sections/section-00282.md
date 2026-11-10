---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.9 ReversalReason <RvslRsn>", "7.4.9.1 Reason <Rsn>"]
file_pages: [390]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.9.1 Reason <Rsn>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 390 to 390.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 390

```text
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
7.4.9.1  Reason <Rsn>
Presence: [1..1]
Definition: Specifies the reason for the reversal.
Reason <Rsn> contains one of the following CorporateActionReversalReason10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 390
Or}   Proprietary <Prtry> [1..1] ± 390
7.4.9.1.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the reason for the reversal.
Datatype: "CorporateActionReversalReason3Code" on page 1203
CodeName Name Definition
DCBD DayCountBasisDifference Difference in day count basis.
FNRC FundsNotReceived Funds have not been received.
IRED IncorrectEntitlementDate Entitlement date is incorrect.
IETR IncorrectEventLevelTaxRate Event level tax rate is incorrect.
IPCU IncorrectPaymentCurrency Payment currency is incorrect.
IPRI IncorrectPrice Price is incorrect.
IVAD IncorrectValueDate Value date is incorrect.
UPAY UnduePayment Payment is not due.
OTHR Other Other
7.4.9.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification for the reason of the reversal.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 390 February 2026
```

