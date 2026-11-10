---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "concept"
source_ids: ["src-000012"]
source_edition: "Version 3.0, 2021-11-03"
concept_id: "bah-signature-guidelines"
message_sets: ["business-application-header"]
message_families: ["head.001"]
message_ids: []
source_locations: ["MUG Annex A pp28–36"]
limitations: ["Illustrative historical technical signature guidelines; authority to sign and required business scenarios are outside scope.", "Source Figure 4 connector ambiguity issue-000017."]
source_editions: ["Version 3.0 2021-11-03"]
---

# BAH signature guidelines in the supplied MUG

The guide’s Annex A is an illustrative technical model for implementation-specific signature guidelines. It does not change business requirements or decide who may sign and which scenarios require signing. Creator and verifiers must agree the signature structure and service/business-area constraints. [§4.1–4.2.3 pp28–31](../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md) (src-000012).

The optional Signature covers the Business Message: BAH plus ISO 20022 Message. The guide does not support signing only part of that Business Message. Signature syntax follows the referenced W3C XML Signature standard with contextual constraints. [§4.2–4.2.1 p28](../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md) (src-000012).

## Structure and references

The illustrative SignedInfo has three Reference elements: ISO message, BAH and KeyInfo. Their order is irrelevant. [§4.2.7 p32](../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md) (src-000012).

| Signed resource | Identifying URI rule | Processing/context | Source |
| --- | --- | --- | --- |
| ISO 20022 Message | URI attribute absent | Application logic selects the ISO message; exclusive canonicalization precedes digest. The guide uses the one URI-absent Reference allowed by its referenced approach. | §4.2.8 p32 |
| BAH | URI attribute present and empty | BAH XML context; sign complete BAH except Signature itself. First transform is enveloped-signature, then exclusive canonicalization. | §4.2.9 pp32–33 |
| KeyInfo | URI fragment references KeyInfo Id | Id should be unique within the enclosing XML document. Exclusive canonicalization precedes digest. Optional Type URI http://www.w3.org/2000/09/xmldsig#KeyInfo need not be further processed. | §4.2.10 p33 |

[§§4.2.7–4.2.10 pp32–33](../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md) (src-000012). The guide claims its added KeyInfo Reference is XAdES-BES compliant; that is retained as a historical source claim, not independently certified.

KeyInfo must contain the X509v3 certificate with the validation key; it may also contain chain certificates according to allowed PKI infrastructure. It recommends no other KeyInfo elements. KeyInfo itself is signed and has an Id with a unique value. Certificate order is irrelevant. The guide recommends the entire chain; where a specific PKI infrastructure is required, the signing certificate alone is sufficient. It notes that using the environment’s trusted CA root may be preferable to checking a supplied root in a fixed-PKI relationship. [§4.2.6 pp31–32](../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md) (src-000012).

## Processing and outcomes

Applications may have approval/amendment steps and may create BAH elements after the ISO message. Calculating SignatureValue is the last Business Message creation step; it may occur in the sending flow if the specified process is preserved. Signature creation/verification uses two defined XML contexts, AppHdr and ISO message (for example Document), independently of transport packaging. [§4.2.11–4.2.12 p33](../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md) (src-000012).

The introductory generic diagram verifies SignatureValue first, then checks the digest. The detailed BAH verification diagram compares the three resource digests before its signature-verification decision. Both source orders are preserved in their own reconstructions. Failed digest comparison or failed verification leads to failure; a successful path requires both. [Figure 2 p29 and explanation p30; Figure 5 p35](../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md) (src-000012).

## Algorithm table and source examples

The source offers RSA/SHA-256, SHA-256 and exclusive canonicalization as an illustrative selection and explicitly anticipates algorithm updates. [Complete algorithm table and literal source spellings](../message-sets/business-application-header/2021-11-03-v3.0/documents/src-000012/tables/tbl-0020.md) preserves all values. This page makes no current cryptographic recommendation. [§4.2.5 p31](../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md) (src-000012).

[Complete retained signature example](../message-sets/business-application-header/2021-11-03-v3.0/documents/src-000012/examples/signature-xml-example.md) preserves the source XML and original page; extracted text has layout artefacts and is not a validated cryptographic fixture. [§4.5 p36](../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md) (src-000012).

## Navigation and unresolved evidence

[Signing flow](../message-sets/business-application-header/2021-11-03-v3.0/flows/signing-business-message.md) · [Verification flow](../message-sets/business-application-header/2021-11-03-v3.0/flows/verifying-signature.md) · [Authorised signatory](../participants/bah-authorised-signatory.md) · [Verifier](../participants/bah-signature-verifier.md)

The page-34 Figure 4 blue connectors appear to map the ISO-message and KeyInfo digests differently from the text and Figure 5. [Figure 4 reconstruction](../message-sets/business-application-header/2021-11-03-v3.0/documents/src-000012/pdf-figures/fig-0033.md) retains the apparent artwork and uncertainty; issue-000017 remains open. The MUG uses V03 examples; applicability to supplied head.001.001.04 remains issue-000004.
