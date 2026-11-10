---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["5 camt.064.001.01 LimitUtilisationJournalQueryV01", "5.4 Message Building Blocks", "5.4.2 SearchCriteria <SchCrit>", "5.4.2.4 LimitCurrency <LmtCcy>"]
file_pages: [71]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.064.001.01"]
---

# 5.4.2.4 LimitCurrency <LmtCcy>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 71 to 71.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 71

```text
AccountIdentification <AcctId> contains one of the following elements (see
"AccountIdentification4Choice" on page 2836 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C2 2837
Or}   Other <Othr> [1..1] ± 2837
5.4.2.4  LimitCurrency <LmtCcy>
Presence: [0..1]
Definition: Currency unit used to specify the limit amount.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 3212
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
5.4.2.5  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Owner of the account which is being queried.
AccountOwner <AcctOwnr> contains the following elements (see "PartyIdentification136" on
page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
5.4.2.6  BilateralLimitCounterpartyIdentification <BilLmtCtrPtyId>
Presence: [1..1]
Definition: Identification of the system member for which the limit is established.
BilateralLimitCounterpartyIdentification <BilLmtCtrPtyId> contains the following elements (see
"SystemPartyIdentification8" on page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.064.001.01 LimitUtilisationJournalQueryV01
Target2-Securities 71 August 2026
```

