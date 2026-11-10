---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["4 Message Items Types"]
file_pages: [40]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4 Message Items Types

Source: [src-000357](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 40 to 40.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 40

```text
4 Message Items Types
4.1 MessageComponents
4.1.1 Account
4.1.1.1  CashAccountType2Choice
Definition: Nature or use of the account.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 40
Or}   Proprietary <Prtry> [1..1] Text 40
4.1.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Account type, in a coded form.
Datatype: "ExternalCashAccountType1Code" on page 76
4.1.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Nature or use of the account in a proprietary form.
Datatype: "Max35Text" on page 83
4.1.1.2  CashAccount40
Definition: Provides the details to identify an account.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 41
   Type <Tp> [0..1] ± 41
   Currency <Ccy> [0..1] CodeSet C2 41
   Name <Nm> [0..1] Text 42
   Proxy <Prxy> [0..1] ± 42
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
40 March 2024
```

