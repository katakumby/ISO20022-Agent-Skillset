---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13", "19.4 Message Building Blocks", "19.4.2 Linkages <Lnkgs>", "19.4.7.5 RemainingToBeSettledAmount <RmngToBeSttldAmt>"]
file_pages: [628]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.025.001.13"]
---

# 19.4.7.5 RemainingToBeSettledAmount <RmngToBeSttldAmt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 628 to 628.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 628

```text
PreviouslySettledAmount <PrevslySttldAmt> contains the following elements (see
"AmountAndDirection52" on page 1368 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C9 1368
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 1368
19.4.7.5  RemainingToBeSettledAmount <RmngToBeSttldAmt>
Presence: [0..1]
Definition: Amount of money remaining to be settled.
RemainingToBeSettledAmount <RmngToBeSttldAmt> contains the following elements (see
"AmountAndDirection52" on page 1368 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C9 1368
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 1368
19.4.7.6  DenominationChoice <DnmtnChc>
Presence: [0..1]
Definition: Denomination of the security to be received or delivered.
Datatype: "Max210Text" on page 2191
19.4.7.7  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "PartyIdentification144" on
page 1664 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1664
   LEI <LEI> [0..1] IdentifierSet 1664
19.4.7.8  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
Approved by the Securities SEG on 27 January 2026 sese.025.001.13
SecuritiesSettlementTransactionConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 628 March 2026
```

