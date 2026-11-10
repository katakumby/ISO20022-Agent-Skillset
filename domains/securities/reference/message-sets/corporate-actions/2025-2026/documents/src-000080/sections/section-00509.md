---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["9 seev.037.001.17 CorporateActionMovementReversalAdviceV17", "9.4 Message Building Blocks", "9.4.4 ReversalReason <RvslRsn>", "9.4.4.1 Reason <Rsn>"]
file_pages: [673]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.037.001.17"]
---

# 9.4.4.1 Reason <Rsn>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 673 to 673.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 673

```text
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
9.4.4.1  Reason <Rsn>
Presence: [1..1]
Definition: Specifies the reason for the reversal.
Reason <Rsn> contains one of the following CorporateActionReversalReason10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 673
Or}   Proprietary <Prtry> [1..1] ± 673
9.4.4.1.1  Code <Cd>
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
9.4.4.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification for the reason of the reversal.
Approved by the Securities SEG on 27 January 2026 seev.037.001.17
CorporateActionMovementReversalAdviceV17
Corporate Actions - Maintenance 2025 - 2026 673 February 2026
```

