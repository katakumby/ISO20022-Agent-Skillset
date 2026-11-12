---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "43.4 Message Building Blocks", "43.4.4 RelatedReference <RltdRef>", "43.4.5.13 BulkCashSettlementDetails <BlkCshSttlmDtls>", "43.4.5.13.1 PaymentInstrument <PmtInstrm>", "43.4.5.13.1.1 CreditTransferDetails <CdtTrfDtls>", "43.4.5.13.1.1.3 DebtorAccount <DbtrAcct>", "43.4.5.13.1.1.3.2 Name <Nm>"]
file_pages: [2068]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
---

# 43.4.5.13.1.1.3.2 Name <Nm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2068 to 2068.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2068

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
43.4.5.13.1.1.3.2  Name <Nm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max35Text" on page 5403
43.4.5.13.1.1.4  DebtorAgent <DbtrAgt>
Presence: [0..1]
Definition: Financial institution servicing an account for the debtor.
DebtorAgent <DbtrAgt> contains the following FinancialInstitutionIdentification17 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1]  2068
{Or     NameAndAddress <NmAndAdr> [1..1] ± 2069
Or     BICFI <BICFI> [1..1] IdentifierSet C7 2069
Or     ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2069
Or}     ProprietaryIdentification <PrtryId> [1..1] Text 2070
   LEI <LEI> [0..1] IdentifierSet 2070
43.4.5.13.1.1.4.1  Party <Pty>
Presence: [1..1]
Definition: Unique identification of the financial institution.
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2068 May 2026
```

