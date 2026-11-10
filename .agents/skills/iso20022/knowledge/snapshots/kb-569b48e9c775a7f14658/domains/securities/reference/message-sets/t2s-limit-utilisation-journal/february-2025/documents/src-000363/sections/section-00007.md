---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LimitUtilisationJournal"
source_ids: ["src-000363"]
source_editions: ["february-2025"]
message_ids: []
heading_path: ["2 camt.064.001.01 LimitUtilisationJournalQueryV01", "2.4 Message Building Blocks", "2.4.2 SearchCriteria <SchCrit>", "2.4.2.4 LimitCurrency <LmtCcy>"]
file_pages: [7]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.064.001.01"]
---

# 2.4.2.4 LimitCurrency <LmtCcy>

Source: [src-000363](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart2_Target2Securities_LimitUtilisationJournal_v1.pdf`. Locator: one-based file pages 7 to 7.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 7

```text
AccountIdentification <AcctId> contains one of the following elements (see
"AccountIdentification4Choice" on page 30 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C4 30
Or}   Other <Othr> [1..1] ± 30
2.4.2.4  LimitCurrency <LmtCcy>
Presence: [0..1]
Definition: Currency unit used to specify the limit amount.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 41
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
2.4.2.5  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Owner of the account which is being queried.
AccountOwner <AcctOwnr> contains the following elements (see "PartyIdentification136" on
page 36 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 36
   LEI <LEI> [0..1] IdentifierSet 36
2.4.2.6  BilateralLimitCounterpartyIdentification <BilLmtCtrPtyId>
Presence: [1..1]
Definition: Identification of the system member for which the limit is established.
BilateralLimitCounterpartyIdentification <BilLmtCtrPtyId> contains the following elements (see
"SystemPartyIdentification8" on page 37 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 37
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 37
Approved by the Securities on the 16th January 2025 and Payments SEG on
the 24th January 2025 under the lead of the Securities SEG.
camt.064.001.01 LimitUtilisationJournalQueryV01
Target2-Securities - Limit Utilisation Journal 7 February 2025
```

