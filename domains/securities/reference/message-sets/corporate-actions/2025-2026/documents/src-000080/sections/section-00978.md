---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.2 Message Datatypes", "16.2.2 CodeSet", "16.2.2.86 NewSecuritiesIssuanceType6Code"]
file_pages: [1222]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.2.2.86 NewSecuritiesIssuanceType6Code

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1222 to 1222.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1222

```text
16.2.2.86  NewSecuritiesIssuanceType6Code
Definition: Specifies the type of securities proceeds; whether they are defeased or non-defeased.
Type: CodeSet
CodeName Name Definition
DEFE DefeasedSecurityIndicator Funds have been placed in escrow by a
trustee or agent to ensure payment on a
portion of the outstanding balance of the
original security on maturity date.
Applicable only in the frame of a Partial
Defeasance PDEF corporate action
event.
NDEF NonDefeasedSecurityIndicator Funds will not be guaranteed at maturity
by the issuer or paying agent for this
newly issued non-defeased security.
Applicable only in the frame of a Partial
Defeasance PDEF corporate action
event.
REFU RefundedSecurityIndicator New security issued that has been
refunded to an earlier maturity date.
Applicable only in the frame of a partial
defeasance PDEF corporate action
event.
NREF NonRefundedSecurityIndicator New Security issued that has not been
refunded and the maturity date of the
original underlying security is
unchanged. Applicable only in the frame
of a Partial Defeasance PDEF corporate
action event.
16.2.2.87  NonEligibleProceedsIndicator1Code
Definition: Specifies information regarding the non eligibility of the outturn resources.
Type: CodeSet
CodeName Name Definition
NELC NonEligibleCurrency Currency not eligible for settlement in the
Central Securities Depository (CSD).
ACLI AccountLimitation Participant's account limitation.
ONEL OtherNonEligibility Other source of non eligibility.
16.2.2.88  NonEligibleProceedsIndicator2Code
Definition: Specifies information regarding the non eligibility of the outturn resources.
Type: CodeSet
CodeName Name Definition
NELC NonEligibleCurrency Currency not eligible for settlement in the
Central Securities Depository (CSD).
ACLI AccountLimitation Participant's account limitation.
ONEL OtherNonEligibility Other source of non eligibility.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1222 February 2026
```

