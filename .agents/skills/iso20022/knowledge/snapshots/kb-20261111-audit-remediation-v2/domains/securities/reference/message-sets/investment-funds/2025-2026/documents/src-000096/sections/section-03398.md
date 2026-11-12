---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.13 SafekeepingAccount2"]
file_pages: [4643]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.13 SafekeepingAccount2

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4643 to 4643.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4643

```text
Definition: Supplementary registration information applying to a specific block of units for dealing and
reporting purposes. The supplementary registration information may be used when all the units are
registered, for example, to a funds supermarket, but holdings for each investor have to reconciled
individually.
Datatype: "Max35Text" on page 5403
66.1.24.13  SafekeepingAccount2
Definition: Safekeeping or investment account. A safekeeping account is an account on which a
securities entry is made. An investment account is an account between an investor(s) and a fund
manager or a fund. The account can contain holdings in any investment fund or investment fund class
managed (or distributed) by the fund manager, within the same fund family.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 4643
   FungibleIndicator <FngbInd> [1..1] Indicator 4643
   Name <Nm> [0..1] Text 4644
   Designation <Dsgnt> [0..1] Text 4644
   IntermediaryInformation <IntrmyInf> [0..10] ± 4644
   AccountOwner <AcctOwnr> [0..1] ± 4644
   AccountServicer <AcctSvcr> [0..1] ± 4645
66.1.24.13.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Identification <Id> contains one of the following elements (see "AccountIdentificationFormatChoice" on
page 4335 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SimpleIdentification <SmplId> [1..1] ± 4335
Or   IdentificationAndPurpose <IdAndPurp> [1..1]  4335
     Identification <Id> [1..1] ± 4336
     Purpose <Purp> [1..1] CodeSet 4336
Or}   IdentificationAsDSS <IdAsDSS> [1..1] ± 4336
66.1.24.13.2  FungibleIndicator <FngbInd>
Presence: [1..1]
Definition: Indicates whether the securities in the account are fungible, ie, interchangeable.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4643 May 2026
```

