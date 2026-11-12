---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.11 CashMovementDetails <CshMvmntDtls>", "8.4.12.11.1 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [618]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.11.1 CreditDebitIndicator <CdtDbtInd>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 618 to 618.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 618

```text
The list of proprietary IssuerOfferorTaxabilityIndicator codes that may be used are provided in the
document " TXAP Taxability Codes" available on the SMPG website at www.smpg.info.
8.4.12.11.1  CreditDebitIndicator <CdtDbtInd>
Presence: [1..1]
Definition: Indicates whether the value is a debit or credit.
Datatype: "CreditDebitCode" on page 1205
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
8.4.12.11.2  ContractualPaymentIndicator <CtrctlPmtInd>
Presence: [0..1]
Definition: Indicates whether the cash payment occurs or will occur in advance of receipt of proceeds
from the issuer and based on a contractual agreement established with the account servicer or upon
receipt of proceeds from the issuer.
Datatype: "Payment1Code" on page 1226
CodeName Name Definition
ACTU ActualPayment The cash payment occurs or will occur
upon receipt of proceeds from the issuer.
CONT ContractualPayment The cash payment occurs or will occur in
advance of receipt of proceeds from the
issuer and based on a contractual
agreement established with the account
servicer.
8.4.12.11.3  IssuerOfferorTaxabilityIndicator <IssrOfferrTaxbltyInd>
Presence: [0..1]
Definition: Proceeds are taxable according to the information provided by the issuer / offeror.
IssuerOfferorTaxabilityIndicator <IssrOfferrTaxbltyInd> contains one of the following
IssuerOfferorTaxabilityIndicator2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 618
Or}   Proprietary <Prtry> [1..1] ± 619
8.4.12.11.3.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify information regarding the issuer / offeror taxability status.
Datatype: "IssuerTaxability2Code" on page 1218
CodeName Name Definition
TXBL Taxable The relevant proceeds are taxable.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 618 February 2026
```

