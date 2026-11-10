---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["32 camt.071.001.05 DeleteStandingOrderV05", "32.4 Message Building Blocks", "32.4.2 StandingOrderDetails <StgOrdrDtls>", "32.4.2.2 AllStandingOrders <AllStgOrdrs>", "32.4.2.2.2 AccountOwner <AcctOwnr>"]
file_pages: [743]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.071.001.05"]
---

# 32.4.2.2.2 AccountOwner <AcctOwnr>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 743 to 743.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 743

```text
Account <Acct> contains the following elements (see "CashAccount40" on page 783 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 783
   Type <Tp> [0..1] ± 783
   Currency <Ccy> [0..1] CodeSet C1 784
   Name <Nm> [0..1] Text 784
   Proxy <Prxy> [0..1] ± 784
Constraints
• IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
• IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
Following Must be True
    /Identification Must be present
 Or    /Proxy Must be present
32.4.2.2.2  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account.
Approved by the Payments SEG on 04 February 2025 camt.071.001.05 DeleteStandingOrderV05
Cash Management - Maintenance 2024 - 2025 743 February 2025
```

