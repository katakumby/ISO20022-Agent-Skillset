---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "5.4 Message Building Blocks", "5.4.3 Modifications <Mods>", "5.4.3.1 AccountOwner <AcctOwnr>"]
file_pages: [109]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 5.4.3.1 AccountOwner <AcctOwnr>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 109 to 109.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 109

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         SettlementQuantity <SttlmQty> [1..1] ± 130
         SettlementAmount <SttlmAmt> [0..1] ± 130
         TradeDate <TradDt> [0..1] ± 131
         SettlementDate <SttlmDt> [1..1] ± 131
         DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C18,
C19,
C20,
C21
131
         ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C18,
C19,
C20,
C21
132
Constraints
• AccountOwnerRule
AccountOwner must be present or Modification(*)/AccountOwner must be present, but not both.
• ProcessingStatusRule
ProcessingStatus must be present or Modification(*)/ProcessingStatus must be present, but not both.
• SafekeepingAccountRule
SafekeepingAccount must be present or Modification(*)/SafekeepingAccount must be present, but
not both.
5.4.3.1  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "SystemPartyIdentification8" on
page 257 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 257
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 257
5.4.3.2  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
Approved by the Securities SEG on 21 August 2025 semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities - Settlement Restrictions 109 September 2025
```

