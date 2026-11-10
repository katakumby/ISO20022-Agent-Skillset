---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.22 RelatedCorporateAction <RltdCorpActn>", "4.4.2.14.18.2.22.2 CorporateActionEventIdentification <CorpActnEvtId>"]
file_pages: [747]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.22.2 CorporateActionEventIdentification <CorpActnEvtId>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 747 to 747.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 747

```text
EventType <EvtTp> contains one of the following elements (see
"CorporateActionEventType104Choice" on page 842 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 843
Or}   Proprietary <Prtry> [1..1] ± 843
Constraints
• EventTypeRule
If Code is present, the code OTHR (Other) must only be used if no other corporate action event code
is appropriate.
If Code is present, the code CHAN (Change) must only be used if no other corporate action event
code is appropriate and only for an event which relates to a change.
If Code is present, the code REDM (Final Maturity) must only be used if the redemption is decided by
the issuer and not by the securities holders.
4.4.2.14.18.2.22.2  CorporateActionEventIdentification <CorpActnEvtId>
Presence: [1..1]
Definition: Reference assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 916
4.4.2.14.18.2.22.3  OfficialCorporateActionEventIdentification <OffclCorpActnEvtId>
Presence: [0..1]
Definition: Official and unique reference assigned by the official central body/entity within each market
at the beginning of a corporate action event.
Datatype: "Max35Text" on page 916
4.4.2.14.18.2.23  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Safekeeping or investment account. A safekeeping account is an account on which a
securities entry is made. An investment account is an account between an investor(s) and a fund
manager or a fund. The account can contain holdings in any investment fund or investment fund class
managed (or distributed) by the fund manager, within the same fund family.
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount19" on
page 800 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 800
   Type <Tp> [0..1] ± 800
   Name <Nm> [0..1] Text 801
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
747 March 2026
```

