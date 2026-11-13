---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "50.4.4.9.22 CashSettlementDetails <CshSttlmDtls>", "50.4.4.9.22.1 PaymentInstrument <PmtInstrm>", "50.4.4.9.22.1.2 CreditTransferDetails <CdtTrfDtls>", "50.4.4.9.22.1.2.3 DebtorAccount <DbtrAcct>", "50.4.4.9.22.1.2.3.2 Name <Nm>"]
file_pages: [3129]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.9.22.1.2.3.2 Name <Nm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3129 to 3129.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3129

```text
Other <Othr> contains the following elements (see "GenericAccountIdentification1" on page 4326 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4326
   SchemeName <SchmeNm> [0..1]  4326
{Or     Code <Cd> [1..1] CodeSet 4326
Or}     Proprietary <Prtry> [1..1] Text 4326
   Issuer <Issr> [0..1] Text 4326
50.4.4.9.22.1.2.3.2  Name <Nm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max35Text" on page 5403
50.4.4.9.22.1.2.4  DebtorAgent <DbtrAgt>
Presence: [0..1]
Definition: Financial institution servicing an account for the debtor.
DebtorAgent <DbtrAgt> contains the following FinancialInstitutionIdentification17 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1]  3129
{Or     NameAndAddress <NmAndAdr> [1..1] ± 3130
Or     BICFI <BICFI> [1..1] IdentifierSet C6 3130
Or     ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3130
Or}     ProprietaryIdentification <PrtryId> [1..1] Text 3131
   LEI <LEI> [0..1] IdentifierSet 3131
50.4.4.9.22.1.2.4.1  Party <Pty>
Presence: [1..1]
Definition: Unique identification of the financial institution.
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3129 May 2026
```

