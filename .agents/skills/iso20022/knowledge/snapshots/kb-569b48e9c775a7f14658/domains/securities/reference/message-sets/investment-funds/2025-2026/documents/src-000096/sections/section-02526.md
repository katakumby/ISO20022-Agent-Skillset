---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.16 RedemptionLegDetails <RedLegDtls>", "53.4.5.16.4 InvestmentAccountDetails <InvstmtAcctDtls>", "53.4.5.16.4.3 AccountDesignation <AcctDsgnt>"]
file_pages: [3561]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.16.4.3 AccountDesignation <AcctDsgnt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3561 to 3561.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3561

```text
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max35Text" on page 5403
53.4.5.16.4.3  AccountDesignation <AcctDsgnt>
Presence: [0..1]
Definition: Supplementary registration information applying to a specific block of units for dealing and
reporting purposes. The supplementary registration information may be used when all the units are
registered, for example, to a funds supermarket, but holdings for each investor have to reconciled
individually.
Datatype: "Max35Text" on page 5403
53.4.5.16.4.4  OwnerIdentification <OwnrId>
Presence: [0..*]
Definition: Party that legally owns the account.
OwnerIdentification <OwnrId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
53.4.5.16.4.5  AccountServicer <AcctSvcr>
Presence: [0..1]
Definition: Party that manages the account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and provides
information about the account.
AccountServicer <AcctSvcr> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
53.4.5.16.4.6  OrderOriginatorEligibility <OrdrOrgtrElgblty>
Presence: [0..1]
Definition: Counterparties eligibility as defined by article 24 of the EU MiFID Directive applicable to
transactions executed by investment firms for eligible counterparties.
Datatype: "OrderOriginatorEligibility1Code" on page 5332
CodeName Name Definition
ELIG Eligible Eligible counterparty - MiFID
classification of counterparty. Eligible
customers are the most sophisticated
level of investor, able to opt out of some
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3561 May 2026
```

