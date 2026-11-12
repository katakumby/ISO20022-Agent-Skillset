---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.4 TradeDetails <TradDtls>", "3.4.4.43 AdditionalTradeInstructionProcessingInformation <AddtlTradInstrPrcgInf>"]
file_pages: [63]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.4.43 AdditionalTradeInstructionProcessingInformation <AddtlTradInstrPrcgInf>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 63 to 63.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 63

```text
AdditionalPhysicalOrRegistrationDetails <AddtlPhysOrRegnDtls> contains the following elements
(see "RegistrationParameters3" on page 246 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CertificationIdentification <CertfctnId> [0..1] Text 246
   CertificationDateTime <CertfctnDtTm> [0..1] ± 246
   RegistrarAccount <RegarAcct> [0..1] Text 246
   CertificateNumber <CertNb> [0..*] ± C21 246
3.4.4.43  AdditionalTradeInstructionProcessingInformation <AddtlTradInstrPrcgInf>
Presence: [0..1]
Definition: Provides additional details of the trade process not included within structured fields of this
message.
Datatype: "Max350Text" on page 669
3.4.5 FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Unique and unambiguous identifier of a financial instrument, assigned under a formal or
proprietary identification scheme.
Impacted by: C19 "DescriptionPresenceRule", C20 "DescriptionUsageRule", C27 "ISINGuideline", C28
"ISINPresenceRule", C34 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification19" on page 270 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 271
   OtherIdentification <OthrId> [0..*]  271
     Identification <Id> [1..1] Text 271
     Suffix <Sfx> [0..1] Text 271
     Type <Tp> [1..1] ± 271
   Description <Desc> [0..1] Text 271
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 63 February 2025
```

