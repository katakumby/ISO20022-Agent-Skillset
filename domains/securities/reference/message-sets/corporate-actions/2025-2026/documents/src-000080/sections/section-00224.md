---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks", "5.4.7 AccountDetails <AcctDtls>", "5.4.7.5 Balance <Bal>", "5.4.7.5.13 InTransshipmentBalance <InTrnsShipmntBal>"]
file_pages: [300]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4.7.5.13 InTransshipmentBalance <InTrnsShipmntBal>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 300 to 300.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 300

```text
TradeDatePositionBalance <TradDtPosBal> contains one of the following elements (see
"BalanceFormat11Choice" on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
5.4.7.5.13  InTransshipmentBalance <InTrnsShipmntBal>
Presence: [0..1]
Definition: Balance of physical securities that are in the process of being transferred from one
depository/agent to another.
InTransshipmentBalance <InTrnsShipmntBal> contains one of the following elements (see
"BalanceFormat11Choice" on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
5.4.7.5.14  RegisteredBalance <RegdBal>
Presence: [0..1]
Definition: Balance of financial instruments that are registered (in the name of a nominee name or of the
beneficial owner).
RegisteredBalance <RegdBal> contains one of the following elements (see
"BalanceFormat11Choice" on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
5.4.8 BeneficialOwnerDetails <BnfclOwnrDtls>
Presence: [0..*]
Definition: Information about the beneficial owner of the securities.
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 300 February 2026
```

